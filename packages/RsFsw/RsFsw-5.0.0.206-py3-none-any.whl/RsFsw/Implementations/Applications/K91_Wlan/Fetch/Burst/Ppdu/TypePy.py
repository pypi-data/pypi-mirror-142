from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:PPDU:TYPE \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.ppdu.typePy.get() \n
		Queries the type of the first analyzed PPDU in the current capture buffer. \n
			:return: ppdu_type: See Table 'Supported modulation formats, PPDU formats and channel bandwidths depending on standard'."""
		response = self._core.io.query_str(f'FETCh:BURSt:PPDU:TYPE?')
		return trim_str_response(response)
