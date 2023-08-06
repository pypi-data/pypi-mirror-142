from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subwindow:
	"""Subwindow commands group definition. 30 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: SubWindow, default value after init: SubWindow.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subwindow", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subWindow_get', 'repcap_subWindow_set', repcap.SubWindow.Nr1)

	def repcap_subWindow_set(self, subWindow: repcap.SubWindow) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubWindow.Default
		Default value after init: SubWindow.Nr1"""
		self._cmd_group.set_repcap_enum_value(subWindow)

	def repcap_subWindow_get(self) -> repcap.SubWindow:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def zoom(self):
		"""zoom commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_zoom'):
			from .Zoom import Zoom
			self._zoom = Zoom(self._core, self._cmd_group)
		return self._zoom

	@property
	def trace(self):
		"""trace commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def notes(self):
		"""notes commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_notes'):
			from .Notes import Notes
			self._notes = Notes(self._core, self._cmd_group)
		return self._notes

	def clone(self) -> 'Subwindow':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Subwindow(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
