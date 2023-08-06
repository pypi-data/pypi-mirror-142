from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


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
		Snippet: driver.applications.k6Pulse.massMemory.store.table.set(columns = enums.StatisticType.ALL, filename = '1', store = repcap.Store.Default) \n
		This command exports result table data from the specified window to an ASCii file (.DAT) . For details on the file format
		see 'Reference: ASCII file export format'. Secure User Mode In secure user mode, settings that are stored on the
		instrument are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory limit reached' error can occur
		although the hard disk indicates that storage space is still available. To store data permanently, select an external
		storage location such as a USB memory device. For details, see 'Protecting Data Using the Secure User Mode'. \n
			:param columns: Columns to be stored in file SELected Export only the selected (visible) table columns ALL Export all table columns (all possible measured parameters)
			:param filename: String containing the path and name of the target file.
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
