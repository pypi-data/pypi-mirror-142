from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Period:
	"""Period commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("period", core, parent)

	def set(self, length: float, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:PERiod \n
		Snippet: driver.sense.sweep.egate.trace.period.set(length = 1.0, trace = repcap.Trace.Default) \n
		This command defines the length of the gate for all traces. The gate length applies to all traces. \n
			:param length: Range: 100 ns to 1000 s, Unit: s
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(length)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:PERiod {param}')

	def get(self, trace=repcap.Trace.Default) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>:PERiod \n
		Snippet: value: float = driver.sense.sweep.egate.trace.period.get(trace = repcap.Trace.Default) \n
		This command defines the length of the gate for all traces. The gate length applies to all traces. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: length: Range: 100 ns to 1000 s, Unit: s"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:PERiod?')
		return Conversions.str_to_float(response)
