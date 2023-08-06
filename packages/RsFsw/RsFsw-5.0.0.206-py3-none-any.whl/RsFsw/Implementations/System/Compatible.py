from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Compatible:
	"""Compatible commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compatible", core, parent)

	def set(self, mode: enums.CompatibilityMode) -> None:
		"""SCPI: SYSTem:COMPatible \n
		Snippet: driver.system.compatible.set(mode = enums.CompatibilityMode.ATT) \n
		This command enables compatibility to other spectrum and signal analyzers by R&S. Compatibility is necessary, for example,
		regarding the number of sweep points. Note that this command is maintained for compatibility reasons only. Use the method
		RsFsw.System.Language.set command for new remote control programs (see method RsFsw.System.Language.set) . \n
			:param mode: DEFault | FSU | FSP | FSQ | FSV
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CompatibilityMode)
		self._core.io.write(f'SYSTem:COMPatible {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CompatibilityMode:
		"""SCPI: SYSTem:COMPatible \n
		Snippet: value: enums.CompatibilityMode = driver.system.compatible.get() \n
		This command enables compatibility to other spectrum and signal analyzers by R&S. Compatibility is necessary, for example,
		regarding the number of sweep points. Note that this command is maintained for compatibility reasons only. Use the method
		RsFsw.System.Language.set command for new remote control programs (see method RsFsw.System.Language.set) . \n
			:return: mode: DEFault | FSU | FSP | FSQ | FSV"""
		response = self._core.io.query_str(f'SYSTem:COMPatible?')
		return Conversions.str_to_scalar_enum(response, enums.CompatibilityMode)
