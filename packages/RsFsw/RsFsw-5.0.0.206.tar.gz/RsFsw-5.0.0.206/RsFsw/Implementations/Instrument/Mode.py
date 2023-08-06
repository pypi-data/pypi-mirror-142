from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, op_mode: enums.InstrumentMode) -> None:
		"""SCPI: INSTrument:MODE \n
		Snippet: driver.instrument.mode.set(op_mode = enums.InstrumentMode.MSRanalyzer) \n
		The operating mode of the R&S FSW determines which applications are available and active. Whenever you change the
		operating mode, the currently active channels are closed. The default operating mode is Signal and Spectrum Analyzer mode,
		however, the presetting can be changed. (See 'Preset Mode') . For details on operating modes and applications see
		'Applications, measurement channels, and operating modes'. \n
			:param op_mode: SANalyzer Signal and Spectrum Analyzer mode MSRanalyzer Multi-Standard Radio Analysis (MSRA) mode RTMStandard Multi-Standard Real-Time (MSRT) mode Only available if one of the real-time options is installed. (See 'Welcome to the R&S FSW Real-Time Extension') .
		"""
		param = Conversions.enum_scalar_to_str(op_mode, enums.InstrumentMode)
		self._core.io.write_with_opc(f'INSTrument:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InstrumentMode:
		"""SCPI: INSTrument:MODE \n
		Snippet: value: enums.InstrumentMode = driver.instrument.mode.get() \n
		The operating mode of the R&S FSW determines which applications are available and active. Whenever you change the
		operating mode, the currently active channels are closed. The default operating mode is Signal and Spectrum Analyzer mode,
		however, the presetting can be changed. (See 'Preset Mode') . For details on operating modes and applications see
		'Applications, measurement channels, and operating modes'. \n
			:return: op_mode: SANalyzer Signal and Spectrum Analyzer mode MSRanalyzer Multi-Standard Radio Analysis (MSRA) mode RTMStandard Multi-Standard Real-Time (MSRT) mode Only available if one of the real-time options is installed. (See 'Welcome to the R&S FSW Real-Time Extension') ."""
		response = self._core.io.query_str_with_opc(f'INSTrument:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.InstrumentMode)
