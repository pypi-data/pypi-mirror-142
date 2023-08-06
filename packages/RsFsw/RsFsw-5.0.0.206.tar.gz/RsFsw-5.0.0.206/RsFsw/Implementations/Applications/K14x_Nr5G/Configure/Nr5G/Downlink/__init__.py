from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Downlink:
	"""Downlink commands group definition. 179 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def cc(self):
		"""cc commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	def clone(self) -> 'Downlink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Downlink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
