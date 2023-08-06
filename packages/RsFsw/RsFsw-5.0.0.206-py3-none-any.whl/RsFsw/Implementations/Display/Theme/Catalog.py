from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self) -> str:
		"""SCPI: DISPlay:THEMe:CATalog \n
		Snippet: value: str = driver.display.theme.catalog.get() \n
		This command queries all available display themes. \n
			:return: themes: String containing all available display themes."""
		response = self._core.io.query_str(f'DISPlay:THEMe:CATalog?')
		return trim_str_response(response)
