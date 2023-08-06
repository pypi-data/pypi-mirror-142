from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Compatible:
	"""Compatible commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compatible", core, parent)

	def set(self, arg_0: enums.PresetCompatible) -> None:
		"""SCPI: SYSTem:PRESet:COMPatible \n
		Snippet: driver.system.preset.compatible.set(arg_0 = enums.PresetCompatible.MRECeiver) \n
		This command defines the operating mode that is activated when you switch on the R&S FSW or press the [PRESET] key. For
		details on operating modes see 'Applications, measurement channels, and operating modes'. \n
			:param arg_0: SANalyzer (Default:) Defines Signal and Spectrum Analyzer operating mode as the presetting. MSRA Defines Multi-Standard Radio Analysis (MSRA) as the preset default operating mode. RTSM Defines Multi-Standard Real-Time (MSRT) as the preset default operating mode.
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.PresetCompatible)
		self._core.io.write(f'SYSTem:PRESet:COMPatible {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PresetCompatible:
		"""SCPI: SYSTem:PRESet:COMPatible \n
		Snippet: value: enums.PresetCompatible = driver.system.preset.compatible.get() \n
		This command defines the operating mode that is activated when you switch on the R&S FSW or press the [PRESET] key. For
		details on operating modes see 'Applications, measurement channels, and operating modes'. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SYSTem:PRESet:COMPatible?')
		return Conversions.str_to_scalar_enum(response, enums.PresetCompatible)
