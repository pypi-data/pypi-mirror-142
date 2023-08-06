from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsignal:
	"""Tsignal commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsignal", core, parent)

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import Awgn
			self._awgn = Awgn(self._core, self._cmd_group)
		return self._awgn

	def clone(self) -> 'Tsignal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tsignal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
