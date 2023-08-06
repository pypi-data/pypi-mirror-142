from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmap:
	"""Cmap commands group definition. 3 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Item, default value after init: Item.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmap", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_item_get', 'repcap_item_set', repcap.Item.Ix1)

	def repcap_item_set(self, item: repcap.Item) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Item.Default
		Default value after init: Item.Ix1"""
		self._cmd_group.set_repcap_enum_value(item)

	def repcap_item_get(self) -> repcap.Item:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def default(self):
		"""default commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_default'):
			from .Default import Default
			self._default = Default(self._core, self._cmd_group)
		return self._default

	@property
	def hsl(self):
		"""hsl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hsl'):
			from .Hsl import Hsl
			self._hsl = Hsl(self._core, self._cmd_group)
		return self._hsl

	@property
	def pdefined(self):
		"""pdefined commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdefined'):
			from .Pdefined import Pdefined
			self._pdefined = Pdefined(self._core, self._cmd_group)
		return self._pdefined

	def clone(self) -> 'Cmap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cmap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
