from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def scs(self):
		"""scs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scs'):
			from .Scs import Scs
			self._scs = Scs(self._core, self._cmd_group)
		return self._scs

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def rset(self):
		"""rset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rset'):
			from .Rset import Rset
			self._rset = Rset(self._core, self._cmd_group)
		return self._rset

	@property
	def rsequence(self):
		"""rsequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsequence'):
			from .Rsequence import Rsequence
			self._rsequence = Rsequence(self._core, self._cmd_group)
		return self._rsequence

	@property
	def zcZone(self):
		"""zcZone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zcZone'):
			from .ZcZone import ZcZone
			self._zcZone = ZcZone(self._core, self._cmd_group)
		return self._zcZone

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
