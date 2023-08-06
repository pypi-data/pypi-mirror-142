from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harmonic:
	"""Harmonic commands group definition. 6 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harmonic", core, parent)

	@property
	def low(self):
		"""low commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_low'):
			from .Low import Low
			self._low = Low(self._core, self._cmd_group)
		return self._low

	@property
	def high(self):
		"""high commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_high'):
			from .High import High
			self._high = High(self._core, self._cmd_group)
		return self._high

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_band'):
			from .Band import Band
			self._band = Band(self._core, self._cmd_group)
		return self._band

	def clone(self) -> 'Harmonic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Harmonic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
