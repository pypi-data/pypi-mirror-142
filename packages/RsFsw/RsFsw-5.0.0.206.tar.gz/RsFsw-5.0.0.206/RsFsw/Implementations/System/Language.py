from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Language:
	"""Language commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("language", core, parent)

	def set(self, language: str) -> None:
		"""SCPI: SYSTem:LANGuage \n
		Snippet: driver.system.language.set(language = '1') \n
		This command selects the system language. For details see 'GPIB languages'. Note:This command is also used to emulate
		previous R&S signal and spectrum analyzers, making the method RsFsw.System.Compatible.set command obsolete. Note: For
		PSA89600 emulation, the option is indicated as 'B7J' for the *OPT? query ('B7J, 140' if 'Wideband' is activated) . Note:
		For R&S FSP/FSQ/FSU emulation, HP commands are not automatically also allowed. In this case, set SYSTem:HPADditional to
		ON. \n
			:param language: 'SCPI' | '8560E' | '8561E' | '8562E' | '8563E' | '8564E' | '8565E' | '8566A' | '8566B' | '8568A' | '8568A_DC' | '8568B' | '8568B_DC' | '8591E' | '8594E' | '71100C' | '71200C' | '71209A' | 'PSA89600' | 'PSA' | 'PXA' | 'FSP' | 'FSU' | 'FSQ' | 'FSV' | 'FSEA' | 'FSEB' | 'FSEM' | 'FSEK'
		"""
		param = Conversions.value_to_quoted_str(language)
		self._core.io.write(f'SYSTem:LANGuage {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:LANGuage \n
		Snippet: value: str = driver.system.language.get() \n
		This command selects the system language. For details see 'GPIB languages'. Note:This command is also used to emulate
		previous R&S signal and spectrum analyzers, making the method RsFsw.System.Compatible.set command obsolete. Note: For
		PSA89600 emulation, the option is indicated as 'B7J' for the *OPT? query ('B7J, 140' if 'Wideband' is activated) . Note:
		For R&S FSP/FSQ/FSU emulation, HP commands are not automatically also allowed. In this case, set SYSTem:HPADditional to
		ON. \n
			:return: language: 'SCPI' | '8560E' | '8561E' | '8562E' | '8563E' | '8564E' | '8565E' | '8566A' | '8566B' | '8568A' | '8568A_DC' | '8568B' | '8568B_DC' | '8591E' | '8594E' | '71100C' | '71200C' | '71209A' | 'PSA89600' | 'PSA' | 'PXA' | 'FSP' | 'FSU' | 'FSQ' | 'FSV' | 'FSEA' | 'FSEB' | 'FSEM' | 'FSEK'"""
		response = self._core.io.query_str(f'SYSTem:LANGuage?')
		return trim_str_response(response)
