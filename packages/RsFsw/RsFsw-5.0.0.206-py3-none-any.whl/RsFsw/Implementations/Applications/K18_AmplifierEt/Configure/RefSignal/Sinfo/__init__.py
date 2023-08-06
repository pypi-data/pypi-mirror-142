from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sinfo:
	"""Sinfo commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	@property
	def cfactor(self):
		"""cfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def fpath(self):
		"""fpath commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpath'):
			from .Fpath import Fpath
			self._fpath = Fpath(self._core, self._cmd_group)
		return self._fpath

	@property
	def obw(self):
		"""obw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_obw'):
			from .Obw import Obw
			self._obw = Obw(self._core, self._cmd_group)
		return self._obw

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import Slength
			self._slength = Slength(self._core, self._cmd_group)
		return self._slength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	def clone(self) -> 'Sinfo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sinfo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
