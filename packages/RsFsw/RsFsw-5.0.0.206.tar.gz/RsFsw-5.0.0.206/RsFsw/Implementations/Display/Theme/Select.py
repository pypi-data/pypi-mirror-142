from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, theme: str) -> None:
		"""SCPI: DISPlay:THEMe:SELect \n
		Snippet: driver.display.theme.select.set(theme = '1') \n
		This command selects the display theme. \n
			:param theme: String containing the name of the theme.
		"""
		param = Conversions.value_to_quoted_str(theme)
		self._core.io.write(f'DISPlay:THEMe:SELect {param}')
