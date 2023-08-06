from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emodel:
	"""Emodel commands group definition. 126 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emodel", core, parent)

	@property
	def riseBasePoint(self):
		"""riseBasePoint commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseBasePoint'):
			from .RiseBasePoint import RiseBasePoint
			self._riseBasePoint = RiseBasePoint(self._core, self._cmd_group)
		return self._riseBasePoint

	@property
	def riseLowPoint(self):
		"""riseLowPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseLowPoint'):
			from .RiseLowPoint import RiseLowPoint
			self._riseLowPoint = RiseLowPoint(self._core, self._cmd_group)
		return self._riseLowPoint

	@property
	def riseMidPoint(self):
		"""riseMidPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseMidPoint'):
			from .RiseMidPoint import RiseMidPoint
			self._riseMidPoint = RiseMidPoint(self._core, self._cmd_group)
		return self._riseMidPoint

	@property
	def riseHighPoint(self):
		"""riseHighPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseHighPoint'):
			from .RiseHighPoint import RiseHighPoint
			self._riseHighPoint = RiseHighPoint(self._core, self._cmd_group)
		return self._riseHighPoint

	@property
	def riseTopPoint(self):
		"""riseTopPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_riseTopPoint'):
			from .RiseTopPoint import RiseTopPoint
			self._riseTopPoint = RiseTopPoint(self._core, self._cmd_group)
		return self._riseTopPoint

	@property
	def fallBasePoint(self):
		"""fallBasePoint commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallBasePoint'):
			from .FallBasePoint import FallBasePoint
			self._fallBasePoint = FallBasePoint(self._core, self._cmd_group)
		return self._fallBasePoint

	@property
	def fallLowPoint(self):
		"""fallLowPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallLowPoint'):
			from .FallLowPoint import FallLowPoint
			self._fallLowPoint = FallLowPoint(self._core, self._cmd_group)
		return self._fallLowPoint

	@property
	def fallMidPoint(self):
		"""fallMidPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallMidPoint'):
			from .FallMidPoint import FallMidPoint
			self._fallMidPoint = FallMidPoint(self._core, self._cmd_group)
		return self._fallMidPoint

	@property
	def fallHighPoint(self):
		"""fallHighPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallHighPoint'):
			from .FallHighPoint import FallHighPoint
			self._fallHighPoint = FallHighPoint(self._core, self._cmd_group)
		return self._fallHighPoint

	@property
	def fallTopPoint(self):
		"""fallTopPoint commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fallTopPoint'):
			from .FallTopPoint import FallTopPoint
			self._fallTopPoint = FallTopPoint(self._core, self._cmd_group)
		return self._fallTopPoint

	def clone(self) -> 'Emodel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emodel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
