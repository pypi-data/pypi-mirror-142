from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	@property
	def maccuracy(self):
		"""maccuracy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_maccuracy'):
			from .Maccuracy import Maccuracy
			self._maccuracy = Maccuracy(self._core, self._cmd_group)
		return self._maccuracy

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def vcurrent(self):
		"""vcurrent commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_vcurrent'):
			from .Vcurrent import Vcurrent
			self._vcurrent = Vcurrent(self._core, self._cmd_group)
		return self._vcurrent

	def set(self, item: enums.TableItemK18, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:STABle:ITEM \n
		Snippet: driver.applications.k18AmplifierEt.display.window.stable.item.set(item = enums.TableItemK18.ADRoop, state = False, window = repcap.Window.Default) \n
		This command adds and removes results from the statistics table. \n
			:param item: Selects the result. See the table in the desription of method RsFsw.Applications.K91_Wlan.Display.Window.Table.Item.set for a list of available parameters.
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.Enum, enums.TableItemK18), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:STABle:ITEM {param}'.rstrip())

	def get(self, item: enums.TableItemK18, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:STABle:ITEM \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.display.window.stable.item.get(item = enums.TableItemK18.ADRoop, window = repcap.Window.Default) \n
		This command adds and removes results from the statistics table. \n
			:param item: Selects the result. See the table in the desription of method RsFsw.Applications.K91_Wlan.Display.Window.Table.Item.set for a list of available parameters.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 1 | 0"""
		param = Conversions.enum_scalar_to_str(item, enums.TableItemK18)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:STABle:ITEM? {param}')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Item':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Item(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
