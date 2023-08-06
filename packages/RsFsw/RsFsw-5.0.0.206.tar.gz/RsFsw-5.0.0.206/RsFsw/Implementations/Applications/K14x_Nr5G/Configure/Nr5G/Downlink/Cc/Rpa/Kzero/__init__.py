from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Kzero:
	"""Kzero commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("kzero", core, parent)

	@property
	def scfe(self):
		"""scfe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scfe'):
			from .Scfe import Scfe
			self._scfe = Scfe(self._core, self._cmd_group)
		return self._scfe

	@property
	def scft(self):
		"""scft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scft'):
			from .Scft import Scft
			self._scft = Scft(self._core, self._cmd_group)
		return self._scft

	@property
	def scns(self):
		"""scns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scns'):
			from .Scns import Scns
			self._scns = Scns(self._core, self._cmd_group)
		return self._scns

	@property
	def scot(self):
		"""scot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scot'):
			from .Scot import Scot
			self._scot = Scot(self._core, self._cmd_group)
		return self._scot

	@property
	def scst(self):
		"""scst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scst'):
			from .Scst import Scst
			self._scst = Scst(self._core, self._cmd_group)
		return self._scst

	@property
	def sctt(self):
		"""sctt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sctt'):
			from .Sctt import Sctt
			self._sctt = Sctt(self._core, self._cmd_group)
		return self._sctt

	def clone(self) -> 'Kzero':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Kzero(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
