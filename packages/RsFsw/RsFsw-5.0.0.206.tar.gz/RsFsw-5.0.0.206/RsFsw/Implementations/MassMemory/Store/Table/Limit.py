from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def set(self, columns: enums.StatisticType, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:TABLe:LIMit \n
		Snippet: driver.massMemory.store.table.limit.set(columns = enums.StatisticType.ALL, filename = '1', store = repcap.Store.Default) \n
		No command help available \n
			:param columns: No help available
			:param filename: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('columns', columns, DataType.Enum, enums.StatisticType), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TABLe:LIMit {param}'.rstrip())
