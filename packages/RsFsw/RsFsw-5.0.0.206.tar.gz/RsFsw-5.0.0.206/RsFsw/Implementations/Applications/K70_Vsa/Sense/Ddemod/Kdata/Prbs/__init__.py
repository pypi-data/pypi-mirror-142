from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prbs:
	"""Prbs commands group definition. 7 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prbs", core, parent)

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def polynomial(self):
		"""polynomial commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_polynomial'):
			from .Polynomial import Polynomial
			self._polynomial = Polynomial(self._core, self._cmd_group)
		return self._polynomial

	@property
	def feedback(self):
		"""feedback commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_feedback'):
			from .Feedback import Feedback
			self._feedback = Feedback(self._core, self._cmd_group)
		return self._feedback

	@property
	def pattern(self):
		"""pattern commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def clone(self) -> 'Prbs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prbs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
