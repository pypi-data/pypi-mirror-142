from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.TraceModeE, trace=repcap.Trace.Default) -> None:
		"""SCPI: CONFigure:ADEMod:RESults:ACV:DETector<det>:MODE \n
		Snippet: driver.configure.ademod.results.acv.detector.mode.set(mode = enums.TraceModeE.AVERage, trace = repcap.Trace.Default) \n
		No command help available \n
			:param mode: No help available
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TraceModeE)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CONFigure:ADEMod:RESults:ACV:DETector{trace_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, trace=repcap.Trace.Default) -> enums.TraceModeE:
		"""SCPI: CONFigure:ADEMod:RESults:ACV:DETector<det>:MODE \n
		Snippet: value: enums.TraceModeE = driver.configure.ademod.results.acv.detector.mode.get(trace = repcap.Trace.Default) \n
		No command help available \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: mode: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CONFigure:ADEMod:RESults:ACV:DETector{trace_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TraceModeE)
