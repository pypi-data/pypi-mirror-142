from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpd:
	"""Dpd commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpd", core, parent)

	@property
	def polynomial(self):
		"""polynomial commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_polynomial'):
			from .Polynomial import Polynomial
			self._polynomial = Polynomial(self._core, self._cmd_group)
		return self._polynomial

	def clone(self) -> 'Dpd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
