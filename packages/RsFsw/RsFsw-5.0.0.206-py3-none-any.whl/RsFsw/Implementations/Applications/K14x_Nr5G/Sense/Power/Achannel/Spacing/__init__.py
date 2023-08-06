from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spacing:
	"""Spacing commands group definition. 9 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spacing", core, parent)

	@property
	def achannel(self):
		"""achannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_achannel'):
			from .Achannel import Achannel
			self._achannel = Achannel(self._core, self._cmd_group)
		return self._achannel

	@property
	def alternate(self):
		"""alternate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alternate'):
			from .Alternate import Alternate
			self._alternate = Alternate(self._core, self._cmd_group)
		return self._alternate

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def gap(self):
		"""gap commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gap'):
			from .Gap import Gap
			self._gap = Gap(self._core, self._cmd_group)
		return self._gap

	@property
	def uaChannel(self):
		"""uaChannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uaChannel'):
			from .UaChannel import UaChannel
			self._uaChannel = UaChannel(self._core, self._cmd_group)
		return self._uaChannel

	@property
	def ualternate(self):
		"""ualternate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ualternate'):
			from .Ualternate import Ualternate
			self._ualternate = Ualternate(self._core, self._cmd_group)
		return self._ualternate

	@property
	def upper(self):
		"""upper commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import Upper
			self._upper = Upper(self._core, self._cmd_group)
		return self._upper

	def clone(self) -> 'Spacing':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spacing(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
