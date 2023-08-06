from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, time: float, trace=repcap.Trace.Default, gateRange=repcap.GateRange.Nr1) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:STARt<gr> \n
		Snippet: driver.sense.sweep.egate.trace.start.set(time = 1.0, trace = repcap.Trace.Default, gateRange = repcap.GateRange.Nr1) \n
		This command defines the start time for a gate range. \n
			:param time: The value range depends on the gate period you have set for the selected trace with [SENSe:]SWEep:EGATe:TRACet:PERiod. The following rules apply: • the start time may not be higher than the length of the gate • the start time may not be lower than the stop time of the gate range of a lower order The reset values depend on the gate range. • for gate range 1, the start time is 0 ms • for gate range 3, the start time is 2 ms • for gate range 5, the start time is 4 ms Unit: s
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:param gateRange: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(time)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		gateRange_cmd_val = self._cmd_group.get_repcap_cmd_value(gateRange, repcap.GateRange)
		self._core.io.write(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:STARt{gateRange_cmd_val} {param}')

	def get(self, trace=repcap.Trace.Default, gateRange=repcap.GateRange.Nr1) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:STARt<gr> \n
		Snippet: value: float = driver.sense.sweep.egate.trace.start.get(trace = repcap.Trace.Default, gateRange = repcap.GateRange.Nr1) \n
		This command defines the start time for a gate range. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:param gateRange: optional repeated capability selector. Default value: Nr1
			:return: time: The value range depends on the gate period you have set for the selected trace with [SENSe:]SWEep:EGATe:TRACet:PERiod. The following rules apply: • the start time may not be higher than the length of the gate • the start time may not be lower than the stop time of the gate range of a lower order The reset values depend on the gate range. • for gate range 1, the start time is 0 ms • for gate range 3, the start time is 2 ms • for gate range 5, the start time is 4 ms Unit: s"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		gateRange_cmd_val = self._cmd_group.get_repcap_cmd_value(gateRange, repcap.GateRange)
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:STARt{gateRange_cmd_val}?')
		return Conversions.str_to_float(response)
