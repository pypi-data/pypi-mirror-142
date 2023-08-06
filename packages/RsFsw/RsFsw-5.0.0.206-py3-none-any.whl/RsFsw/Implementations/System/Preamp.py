from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamp:
	"""Preamp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamp", core, parent)

	def set(self, option: enums.PreampOption) -> None:
		"""SCPI: SYSTem:PREamp \n
		Snippet: driver.system.preamp.set(option = enums.PreampOption.B23) \n
		This setting defines which option is returned when the *OPT? query is executed, depending on the used preamplifier. It is
		only available for FSU/FSQ emulation, and only if an optional preamplifier is used by the R&S FSW. \n
			:param option: B23 | B24
		"""
		param = Conversions.enum_scalar_to_str(option, enums.PreampOption)
		self._core.io.write(f'SYSTem:PREamp {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PreampOption:
		"""SCPI: SYSTem:PREamp \n
		Snippet: value: enums.PreampOption = driver.system.preamp.get() \n
		This setting defines which option is returned when the *OPT? query is executed, depending on the used preamplifier. It is
		only available for FSU/FSQ emulation, and only if an optional preamplifier is used by the R&S FSW. \n
			:return: option: B23 | B24"""
		response = self._core.io.query_str(f'SYSTem:PREamp?')
		return Conversions.str_to_scalar_enum(response, enums.PreampOption)
