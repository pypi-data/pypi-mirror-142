#  Copyright 2022 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging
from functools import cmp_to_key
from math import sqrt, log
from typing import FrozenSet, Tuple, List, Optional, Callable, Dict, Union, Set

from zepben.evolve import Terminal, NetworkService, AcLineSegment, PowerTransformer, EnergyConsumer, \
    PowerTransformerEnd, ConductingEquipment, \
    PowerElectronicsConnection, BusBranchNetworkCreator, EnergySource, Switch, Junction, BusbarSection, PerLengthSequenceImpedance, EquivalentBranch, \
    TransformerFunctionKind, WireInfo, FeederDirection

from zepben.opendss import Bus, LoadConnection
from zepben.opendss import BusConnection, Node
from zepben.opendss import LineCode, Circuit, Line, Load, NetworkModel, Transformer, TransformerWinding
from zepben.opendss.creators.utils import transformer_end_connection_mapper, id_from_identified_objects, get_bus_nodes
from zepben.opendss.creators.validators.validator import OpenDssNetworkValidator

__all__ = ["OpenDssNetworkCreator", "id_from_identified_objects"]

from zepben.opendss.model.network.reg_control import RegControl


def _get_voltage_kv(base_voltage: Union[int, None], bus: Union[Bus, None]):
    if base_voltage is None:
        return 0.0

    if base_voltage == 19100 or base_voltage == 12700 or base_voltage == 6600:
        return base_voltage

    return round((base_voltage / sqrt(3) if bus is not None and len(list(bus.nodes)) == 1 and base_voltage < 1000 else base_voltage) / 1000.0, 3)


def _load_loss_percent(rating_kva: float):
    if rating_kva == 0:
        return 0.0
    value = -0.288 * log(rating_kva) + 2.4293
    if value > 2.2:
        return 2.2
    elif value < 0.5:
        return 0.5
    else:
        return value


def _tx_bus_connection(
        power_transformer: PowerTransformer,
        end: PowerTransformerEnd,
        bus: Union[Bus, None],
        connections: Union[Set[Node], None] = None
):
    # TODO: this mess of code is needed to handle windings connected to nothing, refactor later!
    conn = set() if end.terminal is None else get_bus_nodes(end.terminal) if connections is None else connections
    return BusConnection(Bus(f"{power_transformer.mrid}-disc-end-{end.end_number}", nodes=set()) if bus is None else bus, conn)


def _cmp_end_tn_by_t_direction(end_tn1: Tuple[PowerTransformerEnd, Bus], end_tn2: Tuple[PowerTransformerEnd, Bus]):
    end1, tn1 = end_tn1
    end2, tn2 = end_tn2

    if tn1 is not None and end1 is not None:
        if end1.terminal.normal_feeder_direction.has(FeederDirection.UPSTREAM):
            return -1

    if tn2 is not None and end2 is not None:
        return 1

    return 0


class OpenDssNetworkCreator(
    BusBranchNetworkCreator[NetworkModel, Bus, Line, Line, Transformer, Circuit, Load, Load, OpenDssNetworkValidator]
):

    def __init__(
            self, *,
            logger: logging.Logger,
            vm_pu: float = 1.0,
            load_provider: Callable[[ConductingEquipment], Tuple[float, float]] = lambda x: (0, 0),
            pec_load_provider: Callable[[ConductingEquipment], Tuple[float, float]] = lambda x: (0, 0),
            min_line_r_ohm: float = 0.001,
            min_line_x_ohm: float = 0.001
    ):
        # -- input --
        self.vm_pu = vm_pu
        self.logger = logger
        self.load_provider = load_provider
        self.pec_load_provider = pec_load_provider
        self.min_line_r_ohm = min_line_r_ohm
        self.min_line_x_ohm = min_line_x_ohm

    def bus_branch_network_creator(self, node_breaker_network: NetworkService) -> NetworkModel:
        network = NetworkModel(default_base_frequency=50)
        return network

    def topological_node_creator(
            self,
            bus_branch_network: NetworkModel,
            base_voltage: Optional[int],
            collapsed_conducting_equipment: FrozenSet[ConductingEquipment],
            border_terminals: FrozenSet[Terminal],
            inner_terminals: FrozenSet[Terminal],
            node_breaker_network: NetworkService
    ) -> Tuple[str, Bus]:
        uid = id_from_identified_objects(border_terminals)
        max_phases_terminal = max((t for t in border_terminals), key=lambda t: len(t.phases.single_phases))
        bus = Bus(uid=uid, nodes=get_bus_nodes(max_phases_terminal))
        bus_branch_network.add_bus(bus)
        return uid, bus

    def topological_branch_creator(
            self,
            bus_branch_network: NetworkModel,
            connected_topological_nodes: Tuple[Bus, Bus],
            length: Optional[float],
            collapsed_ac_line_segments: FrozenSet[AcLineSegment],
            border_terminals: FrozenSet[Terminal],
            inner_terminals: FrozenSet[Terminal],
            node_breaker_network: NetworkService
    ) -> Tuple[str, Line]:
        ac_line = next(iter(collapsed_ac_line_segments))
        connected_nodes = min(connected_topological_nodes, key=lambda b: len(b.nodes)).nodes
        line_code = self._get_create_line_code(bus_branch_network, ac_line.per_length_sequence_impedance, ac_line.wire_info, len(connected_nodes))

        uid = id_from_identified_objects(collapsed_ac_line_segments)
        line = Line(
            uid=uid,
            units="m",
            length=0.5 if length is None else length,
            bus_conn1=BusConnection(connected_topological_nodes[0], connected_nodes),
            bus_conn2=BusConnection(connected_topological_nodes[1], connected_nodes),
            line_code=line_code
        )
        bus_branch_network.add_line(line)
        return uid, line

    @staticmethod
    def _get_create_line_code(
            bus_branch_network: NetworkModel,
            per_length_sequence_impedance: PerLengthSequenceImpedance,
            wire_info: WireInfo,
            nphases: int
    ) -> LineCode:
        uid = f"{wire_info.mrid}-{per_length_sequence_impedance.mrid}-{nphases}W"
        line_code = bus_branch_network.line_codes.get(uid)
        if line_code is not None:
            return line_code

        line_code = LineCode(
            uid=uid,
            units="m",
            nphases=nphases,
            r1=per_length_sequence_impedance.r,
            r0=per_length_sequence_impedance.r0,
            x1=per_length_sequence_impedance.x,
            x0=per_length_sequence_impedance.x0,
            c1=0.0,
            c0=0.0,
            norm_amps=wire_info.rated_current,
            emerg_amps=wire_info.rated_current * 1.5
        )
        bus_branch_network.add_line_code(line_code)
        return line_code

    def equivalent_branch_creator(self, bus_branch_network: NetworkModel, connected_topological_nodes: List[Bus], equivalent_branch: EquivalentBranch,
                                  node_breaker_network: NetworkService) -> Tuple[str, Line]:
        raise RuntimeError(
            f"The creation of EquivalentBranches is not supported by the OpenDssNetworkCreator."
            f" Tried to create EquivalentBranches {equivalent_branch.mrid}.")

    def power_transformer_creator(
            self,
            bus_branch_network: NetworkModel,
            power_transformer: PowerTransformer,
            ends_to_topological_nodes: List[Tuple[PowerTransformerEnd, Optional[Bus]]],
            node_breaker_network: NetworkService
    ) -> Dict[str, Transformer]:
        uid = power_transformer.mrid
        num_phases = max([len(get_bus_nodes(end.terminal)) for end, t in ends_to_topological_nodes if end.terminal is not None])

        rating_kva = min(end.rated_s for end in power_transformer.ends) / 1000
        if power_transformer.function is TransformerFunctionKind.voltageRegulator:
            # TODO: this is done to figure out the end to use for the reg_controller as the end number is non-deterministic
            #  for regulators with our current data processing, once we make the bus-branch creator functionality sort terminals
            #  from upstream to downstream this should not be needed anymore.
            ends_to_topological_nodes = sorted(ends_to_topological_nodes, key=cmp_to_key(_cmp_end_tn_by_t_direction))
            transformers_and_reg_controllers = {}
            nodes = max((bus for end, bus in ends_to_topological_nodes), key=lambda b: len(b.nodes)).nodes
            for node in nodes:
                transformer = Transformer(
                    uid=f"{uid}_{str(node)}",
                    phases=1,
                    load_loss_percent=0.001,
                    xhl=0.01,
                    windings=[TransformerWinding(
                        conn="wye",
                        kv=_get_voltage_kv(end.rated_u, bus),
                        kva=1666.7,
                        bus_conn=_tx_bus_connection(power_transformer, end, bus, {node})
                    ) for end, bus in ends_to_topological_nodes]
                )
                bus_branch_network.add_transformer(transformer)
                transformers_and_reg_controllers[transformer.uid] = transformer

                reg_control = RegControl(
                    uid=f"{uid}_controller_{str(node)}",
                    transformer=transformer,
                    winding=len(transformer.windings),
                    vreg=65,
                    band=2,
                    ptratio=100,
                    ctprim=700,
                    r=2,
                    x=7
                )
                bus_branch_network.add_reg_control(reg_control)
                transformers_and_reg_controllers[reg_control.uid] = reg_control

            return transformers_and_reg_controllers
        else:
            ends_to_topological_nodes = sorted(ends_to_topological_nodes, key=lambda end_tn: end_tn[0].end_number)
            transformer = Transformer(
                uid=uid,
                phases=1 if num_phases < 3 else 3,
                load_loss_percent=_load_loss_percent(rating_kva),
                xhl=4,
                windings=[TransformerWinding(
                    conn=transformer_end_connection_mapper(end),
                    kv=_get_voltage_kv(end.rated_u, bus),
                    kva=(end.rated_s or 234000) / 1000.0,
                    bus_conn=_tx_bus_connection(power_transformer, end, bus)
                ) for end, bus in ends_to_topological_nodes]
            )

            bus_branch_network.add_transformer(transformer)
            return {uid: transformer}

    def energy_source_creator(
            self,
            bus_branch_network: NetworkModel,
            energy_source: EnergySource,
            connected_topological_node: Bus,
            node_breaker_network: NetworkService
    ) -> Dict[str, Circuit]:
        if bus_branch_network.circuit is not None:
            raise RuntimeError("Found multiple EnergySources while trying to create OpenDss model. Only one energy source is supported.")

        uid = energy_source.mrid
        circuit = Circuit(
            uid=uid,
            bus_conn=BusConnection(connected_topological_node, connected_topological_node.nodes),
            pu=self.vm_pu,
            base_kv=_get_voltage_kv(energy_source.base_voltage.nominal_voltage, connected_topological_node),
            phases=len(connected_topological_node.nodes)
        )
        bus_branch_network.set_circuit(circuit)
        return {uid: circuit}

    def energy_consumer_creator(
            self, bus_branch_network: NetworkModel,
            energy_consumer: EnergyConsumer,
            connected_topological_node: Bus,
            node_breaker_network: NetworkService
    ) -> Dict[str, Load]:
        uid = energy_consumer.mrid
        load = LoadConnection(
            uid=uid,
            bus_conn=BusConnection(connected_topological_node, connected_topological_node.nodes),
            kv=_get_voltage_kv(energy_consumer.base_voltage.nominal_voltage, connected_topological_node),
            phases=len(connected_topological_node.nodes)
        )
        bus_branch_network.add_load_connection(load)
        return {uid: load}

    def power_electronics_connection_creator(
            self,
            bus_branch_network: NetworkModel,
            power_electronics_connection: PowerElectronicsConnection,
            connected_topological_node: Bus,
            node_breaker_network: NetworkService,
    ) -> Dict[str, Load]:
        uid = power_electronics_connection.mrid
        return {uid: None}

    def has_negligible_impedance(self, ce: ConductingEquipment) -> bool:
        if isinstance(ce, AcLineSegment):
            if ce.length == 0 or ce.per_length_sequence_impedance.r == 0:
                return True

            if ce.length * ce.per_length_sequence_impedance.r < self.min_line_r_ohm \
                    or ce.length * ce.per_length_sequence_impedance.x < self.min_line_x_ohm:
                return True

            return False
        if isinstance(ce, Switch):
            return not ce.is_open()
        if isinstance(ce, Junction) or isinstance(ce, BusbarSection) or isinstance(ce, EquivalentBranch):
            return True
        return False

    def validator_creator(self) -> OpenDssNetworkValidator:
        return OpenDssNetworkValidator(logger=self.logger)
