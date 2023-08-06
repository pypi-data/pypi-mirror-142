from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:PATTern:MAPPing:CATalog \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.pattern.mapping.catalog.get() \n
		This command queries the names of all mappings that are available for the pattern for the current modulation type and
		order. A mapping describes the assignment of constellation points to symbols. This command is only available if the
		additional Multi-Modulation Analysis option (R&S FSW-K70M) is installed. \n
			:return: mappings: list A comma-separated list of strings, with one string for each mapping name."""
		response = self._core.io.query_str(f'SENSe:DDEMod:PATTern:MAPPing:CATalog?')
		return trim_str_response(response)
