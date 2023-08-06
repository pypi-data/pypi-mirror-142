from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Formatted:
	"""Formatted commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatted", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:ALL:FORMatted \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.all.formatted.get() \n
		This command returns all results from the default WLAN measurement (Modulation Accuracy, Flatness and Tolerance.
		For details see 'Modulation accuracy, flatness and tolerance parameters'. The results are output as a list of result
		strings separated by commas in ASCII format. The results are output in the following order: <Global Result>, <Stream 1
		result> ... <Stream n result> \n
			:return: global_result: list preamble power, payload power, peak power, 'nan','nan','nan', 'nan','nan','nan', min freq error,avg freq error, max freq error, min symbol error, avg symbol error, max symbol error, 'nan','nan','nan', 'nan','nan','nan', 'nan','nan','nan', min EVM all, avg EVM all, max EVM all, min EVM data, avg EVM data , max EVM data min EVM pilots, avg EVM pilots , max EVM pilots 'nan','nan','nan', 'nan','nan','nan', 'nan','nan','nan', 'nan','nan','nan',"""
		response = self._core.io.query_str(f'FETCh:BURSt:ALL:FORMatted?')
		return trim_str_response(response)
