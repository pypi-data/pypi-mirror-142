from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srs:
	"""Srs commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def anst(self):
		"""anst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anst'):
			from .Anst import Anst
			self._anst = Anst(self._core, self._cmd_group)
		return self._anst

	@property
	def bhop(self):
		"""bhop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bhop'):
			from .Bhop import Bhop
			self._bhop = Bhop(self._core, self._cmd_group)
		return self._bhop

	@property
	def bsrs(self):
		"""bsrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsrs'):
			from .Bsrs import Bsrs
			self._bsrs = Bsrs(self._core, self._cmd_group)
		return self._bsrs

	@property
	def csrs(self):
		"""csrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csrs'):
			from .Csrs import Csrs
			self._csrs = Csrs(self._core, self._cmd_group)
		return self._csrs

	@property
	def cycs(self):
		"""cycs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycs'):
			from .Cycs import Cycs
			self._cycs = Cycs(self._core, self._cmd_group)
		return self._cycs

	@property
	def isrs(self):
		"""isrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isrs'):
			from .Isrs import Isrs
			self._isrs = Isrs(self._core, self._cmd_group)
		return self._isrs

	@property
	def mupt(self):
		"""mupt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mupt'):
			from .Mupt import Mupt
			self._mupt = Mupt(self._core, self._cmd_group)
		return self._mupt

	@property
	def nrrc(self):
		"""nrrc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrrc'):
			from .Nrrc import Nrrc
			self._nrrc = Nrrc(self._core, self._cmd_group)
		return self._nrrc

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def stat(self):
		"""stat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stat'):
			from .Stat import Stat
			self._stat = Stat(self._core, self._cmd_group)
		return self._stat

	@property
	def suConfig(self):
		"""suConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_suConfig'):
			from .SuConfig import SuConfig
			self._suConfig = SuConfig(self._core, self._cmd_group)
		return self._suConfig

	@property
	def trComb(self):
		"""trComb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trComb'):
			from .TrComb import TrComb
			self._trComb = TrComb(self._core, self._cmd_group)
		return self._trComb

	def clone(self) -> 'Srs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Srs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
