from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	def set(self, columns: enums.StatisticType, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:TABLe \n
		Snippet: driver.massMemory.store.table.set(columns = enums.StatisticType.ALL, filename = '1', store = repcap.Store.Default) \n
		No command help available \n
			:param columns: No help available
			:param filename: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('columns', columns, DataType.Enum, enums.StatisticType), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TABLe {param}'.rstrip())

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
