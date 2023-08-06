from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def hopping(self):
		"""hopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopping'):
			from .Hopping import Hopping
			self._hopping = Hopping(self._core, self._cmd_group)
		return self._hopping

	@property
	def fhopping(self):
		"""fhopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhopping'):
			from .Fhopping import Fhopping
			self._fhopping = Fhopping(self._core, self._cmd_group)
		return self._fhopping

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
