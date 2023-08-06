from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subwindow:
	"""Subwindow commands group definition. 19 total commands, 7 Subgroups, 0 group commands
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
	def ccNumber(self):
		"""ccNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccNumber'):
			from .CcNumber import CcNumber
			self._ccNumber = CcNumber(self._core, self._cmd_group)
		return self._ccNumber

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import Coupling
			self._coupling = Coupling(self._core, self._cmd_group)
		return self._coupling

	@property
	def fnumber(self):
		"""fnumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fnumber'):
			from .Fnumber import Fnumber
			self._fnumber = Fnumber(self._core, self._cmd_group)
		return self._fnumber

	@property
	def isnumber(self):
		"""isnumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isnumber'):
			from .Isnumber import Isnumber
			self._isnumber = Isnumber(self._core, self._cmd_group)
		return self._isnumber

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .Size import Size
			self._size = Size(self._core, self._cmd_group)
		return self._size

	@property
	def trace(self):
		"""trace commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	def clone(self) -> 'Subwindow':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Subwindow(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
