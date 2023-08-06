from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 4 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: HalfDecadeRange, default value after init: HalfDecadeRange.Rng_1Hz_3Hz"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_halfDecadeRange_get', 'repcap_halfDecadeRange_set', repcap.HalfDecadeRange.Rng_1Hz_3Hz)

	def repcap_halfDecadeRange_set(self, halfDecadeRange: repcap.HalfDecadeRange) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HalfDecadeRange.Default
		Default value after init: HalfDecadeRange.Rng_1Hz_3Hz"""
		self._cmd_group.set_repcap_enum_value(halfDecadeRange)

	def repcap_halfDecadeRange_get(self) -> repcap.HalfDecadeRange:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bandwidth(self):
		"""bandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def iqWindow(self):
		"""iqWindow commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqWindow'):
			from .IqWindow import IqWindow
			self._iqWindow = IqWindow(self._core, self._cmd_group)
		return self._iqWindow

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	def clone(self) -> 'Range':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Range(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
