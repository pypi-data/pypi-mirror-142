from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Logo:
	"""Logo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logo", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: DISPlay:LOGO \n
		Snippet: driver.display.logo.set(state = False) \n
		Activates/deactivates the printout of the Rohde & Schwarz company logo at the top of each page. \n
			:param state: 1 | 0 | ON | OFF 1 | ON Logo is printed. 0 | OFF Logo is not printed.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:LOGO {param}')

	def get(self) -> bool:
		"""SCPI: DISPlay:LOGO \n
		Snippet: value: bool = driver.display.logo.get() \n
		Activates/deactivates the printout of the Rohde & Schwarz company logo at the top of each page. \n
			:return: state: 1 | 0 | ON | OFF 1 | ON Logo is printed. 0 | OFF Logo is not printed."""
		response = self._core.io.query_str(f'DISPlay:LOGO?')
		return Conversions.str_to_bool(response)
