from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Function:
	"""Function commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	def set(self, state: bool, trace=repcap.Trace.Default) -> None:
		"""SCPI: [SENSe]:DETector<t>:DEFault[:FUNCtion] \n
		Snippet: driver.applications.k18AmplifierEt.sense.detector.default.function.set(state = False, trace = repcap.Trace.Default) \n
		Selects the default detector for result displays. \n
			:param state: AVERage | OFF
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.bool_to_str(state)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'SENSe:DETector{trace_cmd_val}:DEFault:FUNCtion {param}')

	def get(self, trace=repcap.Trace.Default) -> bool:
		"""SCPI: [SENSe]:DETector<t>:DEFault[:FUNCtion] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.detector.default.function.get(trace = repcap.Trace.Default) \n
		Selects the default detector for result displays. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: state: AVERage | OFF"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:DETector{trace_cmd_val}:DEFault:FUNCtion?')
		return Conversions.str_to_bool(response)
