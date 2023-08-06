from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	def set(self, columns: enums.StatisticType, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:TABLe \n
		Snippet: driver.applications.k50Spurious.massMemory.store.table.set(columns = enums.StatisticType.ALL, filename = '1', store = repcap.Store.Default) \n
		Exports the selected data from the specified window as a comma-separated list of results, table row by table row, to an
		ASCII file. The decimal separator (decimal point or comma) for floating-point numerals contained in the file is defined
		by method RsFsw.Applications.K10x_Lte.FormatPy.Dexport.Dseparator.set. \n
			:param columns: SELected | ALL Defines which columns to include in the export file. SELected Only the results defined by method RsFsw.Applications.K50_Spurious.Calculate.Ssearch.Table.Column.set are included. ALL All available results are included.
			:param filename: String containing the path and name of the file.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('columns', columns, DataType.Enum, enums.StatisticType), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TABLe {param}'.rstrip())
