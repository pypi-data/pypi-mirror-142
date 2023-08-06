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
	"""Item commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def set(self, item: enums.ResultItemK18, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:PTABle:ITEM \n
		Snippet: driver.applications.k18AmplifierEt.display.window.ptable.item.set(item = enums.ResultItemK18.ACB1, state = False, window = repcap.Window.Default) \n
		This command adds and removes results from the Parameter Sweep Table. \n
			:param item: Selects the result. See the table at method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Z.Result.set for a list of available parameters.
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('item', item, DataType.Enum, enums.ResultItemK18), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:PTABle:ITEM {param}'.rstrip())

	def get(self, item: enums.ResultItemK18, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:PTABle:ITEM \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.display.window.ptable.item.get(item = enums.ResultItemK18.ACB1, window = repcap.Window.Default) \n
		This command adds and removes results from the Parameter Sweep Table. \n
			:param item: Selects the result. See the table at method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Z.Result.set for a list of available parameters.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 1 | 0"""
		param = Conversions.enum_scalar_to_str(item, enums.ResultItemK18)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:PTABle:ITEM? {param}')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Item':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Item(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
