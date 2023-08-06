from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cestimation:
	"""Cestimation commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cestimation", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def loComp(self):
		"""loComp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loComp'):
			from .LoComp import LoComp
			self._loComp = LoComp(self._core, self._cmd_group)
		return self._loComp

	@property
	def cdecimation(self):
		"""cdecimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdecimation'):
			from .Cdecimation import Cdecimation
			self._cdecimation = Cdecimation(self._core, self._cmd_group)
		return self._cdecimation

	@property
	def mcOffset(self):
		"""mcOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcOffset'):
			from .McOffset import McOffset
			self._mcOffset = McOffset(self._core, self._cmd_group)
		return self._mcOffset

	@property
	def mvelocity(self):
		"""mvelocity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mvelocity'):
			from .Mvelocity import Mvelocity
			self._mvelocity = Mvelocity(self._core, self._cmd_group)
		return self._mvelocity

	@property
	def vtolerance(self):
		"""vtolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vtolerance'):
			from .Vtolerance import Vtolerance
			self._vtolerance = Vtolerance(self._core, self._cmd_group)
		return self._vtolerance

	@property
	def transmission(self):
		"""transmission commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transmission'):
			from .Transmission import Transmission
			self._transmission = Transmission(self._core, self._cmd_group)
		return self._transmission

	def clone(self) -> 'Cestimation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cestimation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
