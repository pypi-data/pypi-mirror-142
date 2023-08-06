from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Column:
	"""Column commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("column", core, parent)

	def set(self, state: bool, headers: List[enums.HeadersK50]) -> None:
		"""SCPI: CALCulate:SSEarch:TABLe:COLumn \n
		Snippet: driver.applications.k50Spurious.calculate.ssearch.table.column.set(state = False, headers = [HeadersK50.ALL, HeadersK50.STOP]) \n
		Select the numerical results to be displayed in the Spurious Detection Table. For a description of the individual results
		see 'Spurious Detection Table'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Hides the result ON | 1 Displays the result
			:param headers: ALL | SID | STARt | STOP | RBW | FREQuency | POWer | DELTa | IDENt ALL All available results are displayed STARt Start frequency of range/span STOP Stop frequency of range/span FREQuency Spur frequency POWer Spur power DELTa Delta of spur to limit RBW Resolution bandwidth used for range IDENt Spur ID
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle.as_open_list('headers', headers, DataType.EnumList, enums.HeadersK50))
		self._core.io.write(f'CALCulate:SSEarch:TABLe:COLumn {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self) -> List[enums.HeadersK50]:
		"""SCPI: CALCulate:SSEarch:TABLe:COLumn \n
		Snippet: value: List[enums.HeadersK50] = driver.applications.k50Spurious.calculate.ssearch.table.column.get() \n
		Select the numerical results to be displayed in the Spurious Detection Table. For a description of the individual results
		see 'Spurious Detection Table'. \n
			:return: headers: ALL | SID | STARt | STOP | RBW | FREQuency | POWer | DELTa | IDENt ALL All available results are displayed STARt Start frequency of range/span STOP Stop frequency of range/span FREQuency Spur frequency POWer Spur power DELTa Delta of spur to limit RBW Resolution bandwidth used for range IDENt Spur ID"""
		response = self._core.io.query_str(f'CALCulate:SSEarch:TABLe:COLumn?')
		return Conversions.str_to_list_enum(response, enums.HeadersK50)
