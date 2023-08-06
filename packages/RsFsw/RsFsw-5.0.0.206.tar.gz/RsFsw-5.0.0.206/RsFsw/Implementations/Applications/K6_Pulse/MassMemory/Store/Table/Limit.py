from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def set(self, columns: enums.StatisticType, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:TABLe:LIMit \n
		Snippet: driver.applications.k6Pulse.massMemory.store.table.limit.set(columns = enums.StatisticType.ALL, filename = '1', store = repcap.Store.Default) \n
		This command stores the table columns (all or selected) , along with limit check results in a file with ASCII format. The
		decimal separator (decimal point or comma) for floating-point numerals contained in the file is defined with the method
		RsFsw.Applications.K10x_Lte.FormatPy.Dexport.Dseparator.set command. \n
			:param columns: SELected | ALL SELected Only the currently visible columns in the result display are exported. ALL All columns, including currently hidden ones, for the result display are exported.
			:param filename: String containing the path and name of the file.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('columns', columns, DataType.Enum, enums.StatisticType), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TABLe:LIMit {param}'.rstrip())
