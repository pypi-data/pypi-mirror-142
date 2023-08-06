from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Function:
	"""Function commands group definition. 20 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	@property
	def afPhase(self):
		"""afPhase commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_afPhase'):
			from .AfPhase import AfPhase
			self._afPhase = AfPhase(self._core, self._cmd_group)
		return self._afPhase

	@property
	def fixed(self):
		"""fixed commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fixed'):
			from .Fixed import Fixed
			self._fixed = Fixed(self._core, self._cmd_group)
		return self._fixed

	@property
	def pnoise(self):
		"""pnoise commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pnoise'):
			from .Pnoise import Pnoise
			self._pnoise = Pnoise(self._core, self._cmd_group)
		return self._pnoise

	@property
	def bpower(self):
		"""bpower commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpower'):
			from .Bpower import Bpower
			self._bpower = Bpower(self._core, self._cmd_group)
		return self._bpower

	@property
	def fmeasurement(self):
		"""fmeasurement commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmeasurement'):
			from .Fmeasurement import Fmeasurement
			self._fmeasurement = Fmeasurement(self._core, self._cmd_group)
		return self._fmeasurement

	def clone(self) -> 'Function':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Function(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
