from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: GateRange, default value after init: GateRange.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_gateRange_get', 'repcap_gateRange_set', repcap.GateRange.Nr1)

	def repcap_gateRange_set(self, gateRange: repcap.GateRange) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GateRange.Default
		Default value after init: GateRange.Nr1"""
		self._cmd_group.set_repcap_enum_value(gateRange)

	def repcap_gateRange_get(self) -> repcap.GateRange:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, time: float, trace=repcap.Trace.Default, gateRange=repcap.GateRange.Default) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:STOP<gr> \n
		Snippet: driver.sense.sweep.egate.trace.stop.set(time = 1.0, trace = repcap.Trace.Default, gateRange = repcap.GateRange.Default) \n
		This command defines the stop time for a gate range. \n
			:param time: The value range depends on the gate period you have set for the selected trace with [SENSe:]SWEep:EGATe:TRACet:PERiod. The following rules apply: • the stop time may not be higher than the length of the gate • the stop time may not be lower than the start time The reset values depend on the gate range. • for gate range 1, the stop time is 1 ms • for gate range 3, the stop time is 3 ms • for gate range 5, the stop time is 5 ms Unit: s
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:param gateRange: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stop')
		"""
		param = Conversions.decimal_value_to_str(time)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		gateRange_cmd_val = self._cmd_group.get_repcap_cmd_value(gateRange, repcap.GateRange)
		self._core.io.write(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:STOP{gateRange_cmd_val} {param}')

	def get(self, trace=repcap.Trace.Default, gateRange=repcap.GateRange.Default) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:STOP<gr> \n
		Snippet: value: float = driver.sense.sweep.egate.trace.stop.get(trace = repcap.Trace.Default, gateRange = repcap.GateRange.Default) \n
		This command defines the stop time for a gate range. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:param gateRange: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stop')
			:return: time: The value range depends on the gate period you have set for the selected trace with [SENSe:]SWEep:EGATe:TRACet:PERiod. The following rules apply: • the stop time may not be higher than the length of the gate • the stop time may not be lower than the start time The reset values depend on the gate range. • for gate range 1, the stop time is 1 ms • for gate range 3, the stop time is 3 ms • for gate range 5, the stop time is 5 ms Unit: s"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		gateRange_cmd_val = self._cmd_group.get_repcap_cmd_value(gateRange, repcap.GateRange)
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:STOP{gateRange_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Stop':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stop(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
