from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	def set(self, item: enums.TableItemK91, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: driver.applications.k91Wlan.display.window.table.item.set(item = enums.TableItemK91.BPILot, state = False, window = repcap.Window.Default) \n
		Defines which items are displayed in the Result Summary (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the Result Summary. \n
			:param item: Item to be included in Result Summary. For an overview of possible results and the required parameters see the tables below.
			:param state: ON | OFF | 0 | 1 OFF | 0 Item is displayed in Result Summary. ON | 1 Item is not displayed in Result Summary.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.Enum, enums.TableItemK91), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM {param}'.rstrip())

	# noinspection PyTypeChecker
	class ItemStruct(StructBase):
		"""Response structure. Fields: \n
			- Item: enums.TableItemK91: Item to be included in Result Summary. For an overview of possible results and the required parameters see the tables below.
			- State: bool: ON | OFF | 0 | 1 OFF | 0 Item is displayed in Result Summary. ON | 1 Item is not displayed in Result Summary."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Item', enums.TableItemK91),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Item: enums.TableItemK91 = None
			self.State: bool = None

	def get(self, window=repcap.Window.Default) -> ItemStruct:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: value: ItemStruct = driver.applications.k91Wlan.display.window.table.item.get(window = repcap.Window.Default) \n
		Defines which items are displayed in the Result Summary (see 'Result Summary Detailed' and 'Result Summary Global') .
		Note that the results are always calculated, regardless of their visibility in the Result Summary. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: structure: for return value, see the help for ItemStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM?', self.__class__.ItemStruct())
