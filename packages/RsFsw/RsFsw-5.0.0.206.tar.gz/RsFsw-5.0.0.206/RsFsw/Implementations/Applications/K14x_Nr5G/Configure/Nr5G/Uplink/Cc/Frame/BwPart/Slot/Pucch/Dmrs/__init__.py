from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dmrs:
	"""Dmrs commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def ghopping(self):
		"""ghopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ghopping'):
			from .Ghopping import Ghopping
			self._ghopping = Ghopping(self._core, self._cmd_group)
		return self._ghopping

	@property
	def hid(self):
		"""hid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hid'):
			from .Hid import Hid
			self._hid = Hid(self._core, self._cmd_group)
		return self._hid

	@property
	def icShift(self):
		"""icShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_icShift'):
			from .IcShift import IcShift
			self._icShift = IcShift(self._core, self._cmd_group)
		return self._icShift

	@property
	def isfHopping(self):
		"""isfHopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isfHopping'):
			from .IsfHopping import IsfHopping
			self._isfHopping = IsfHopping(self._core, self._cmd_group)
		return self._isfHopping

	@property
	def nid(self):
		"""nid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nid'):
			from .Nid import Nid
			self._nid = Nid(self._core, self._cmd_group)
		return self._nid

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Sgeneration import Sgeneration
			self._sgeneration = Sgeneration(self._core, self._cmd_group)
		return self._sgeneration

	@property
	def shPrb(self):
		"""shPrb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shPrb'):
			from .ShPrb import ShPrb
			self._shPrb = ShPrb(self._core, self._cmd_group)
		return self._shPrb

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import Sid
			self._sid = Sid(self._core, self._cmd_group)
		return self._sid

	@property
	def tdoIndex(self):
		"""tdoIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdoIndex'):
			from .TdoIndex import TdoIndex
			self._tdoIndex = TdoIndex(self._core, self._cmd_group)
		return self._tdoIndex

	def clone(self) -> 'Dmrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dmrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
