from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 23 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def impedance(self):
		"""impedance commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_impedance'):
			from .Impedance import Impedance
			self._impedance = Impedance(self._core, self._cmd_group)
		return self._impedance

	@property
	def osc(self):
		"""osc commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_osc'):
			from .Osc import Osc
			self._osc = Osc(self._core, self._cmd_group)
		return self._osc

	@property
	def balanced(self):
		"""balanced commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_balanced'):
			from .Balanced import Balanced
			self._balanced = Balanced(self._core, self._cmd_group)
		return self._balanced

	@property
	def fullscale(self):
		"""fullscale commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fullscale'):
			from .Fullscale import Fullscale
			self._fullscale = Fullscale(self._core, self._cmd_group)
		return self._fullscale

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
