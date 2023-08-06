from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def mac(self):
		"""mac commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import Mac
			self._mac = Mac(self._core, self._cmd_group)
		return self._mac

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def payload(self):
		"""payload commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import Payload
			self._payload = Payload(self._core, self._cmd_group)
		return self._payload

	@property
	def phrRate(self):
		"""phrRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phrRate'):
			from .PhrRate import PhrRate
			self._phrRate = PhrRate(self._core, self._cmd_group)
		return self._phrRate

	@property
	def sts(self):
		"""sts commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import Sts
			self._sts = Sts(self._core, self._cmd_group)
		return self._sts

	def clone(self) -> 'Demod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Demod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
