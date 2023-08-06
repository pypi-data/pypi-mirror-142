from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, trace=repcap.Trace.Default) -> None:
		"""SCPI: CONFigure:ADEMod:RESults:AM:DETector<det>:STATe \n
		Snippet: driver.configure.ademod.results.am.detector.state.set(state = False, trace = repcap.Trace.Default) \n
		Activates relative demodulation for the selected detector. If activated, the demodulated result is set in relation to the
		reference value defined by method RsFsw.Configure.Ademod.Results.Pm.Detector.Reference.set. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.bool_to_str(state)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CONFigure:ADEMod:RESults:AM:DETector{trace_cmd_val}:STATe {param}')

	def get(self, trace=repcap.Trace.Default) -> bool:
		"""SCPI: CONFigure:ADEMod:RESults:AM:DETector<det>:STATe \n
		Snippet: value: bool = driver.configure.ademod.results.am.detector.state.get(trace = repcap.Trace.Default) \n
		Activates relative demodulation for the selected detector. If activated, the demodulated result is set in relation to the
		reference value defined by method RsFsw.Configure.Ademod.Results.Pm.Detector.Reference.set. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CONFigure:ADEMod:RESults:AM:DETector{trace_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
