from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def master(self):
		"""master commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_master'):
			from .Master import Master
			self._master = Master(self._core, self._cmd_group)
		return self._master

	@property
	def sender(self):
		"""sender commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sender'):
			from .Sender import Sender
			self._sender = Sender(self._core, self._cmd_group)
		return self._sender

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
