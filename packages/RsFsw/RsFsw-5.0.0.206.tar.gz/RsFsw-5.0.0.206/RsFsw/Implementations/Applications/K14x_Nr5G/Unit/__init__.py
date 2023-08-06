from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 8 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	@property
	def bstream(self):
		"""bstream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bstream'):
			from .Bstream import Bstream
			self._bstream = Bstream(self._core, self._cmd_group)
		return self._bstream

	@property
	def caReference(self):
		"""caReference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caReference'):
			from .CaReference import CaReference
			self._caReference = CaReference(self._core, self._cmd_group)
		return self._caReference

	@property
	def caxes(self):
		"""caxes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caxes'):
			from .Caxes import Caxes
			self._caxes = Caxes(self._core, self._cmd_group)
		return self._caxes

	@property
	def evm(self):
		"""evm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def opower(self):
		"""opower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_opower'):
			from .Opower import Opower
			self._opower = Opower(self._core, self._cmd_group)
		return self._opower

	@property
	def pmeter(self):
		"""pmeter commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def saxes(self):
		"""saxes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_saxes'):
			from .Saxes import Saxes
			self._saxes = Saxes(self._core, self._cmd_group)
		return self._saxes

	def clone(self) -> 'Unit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Unit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
