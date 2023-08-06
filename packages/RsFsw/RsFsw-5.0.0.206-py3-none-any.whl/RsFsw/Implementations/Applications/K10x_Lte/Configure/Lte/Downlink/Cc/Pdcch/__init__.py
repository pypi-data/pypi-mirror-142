from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdcch:
	"""Pdcch commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def nopd(self):
		"""nopd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nopd'):
			from .Nopd import Nopd
			self._nopd = Nopd(self._core, self._cmd_group)
		return self._nopd

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

	def clone(self) -> 'Pdcch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdcch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
