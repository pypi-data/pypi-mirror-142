from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pucch:
	"""Pucch commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	@property
	def deShift(self):
		"""deShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deShift'):
			from .DeShift import DeShift
			self._deShift = DeShift(self._core, self._cmd_group)
		return self._deShift

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def n1Cs(self):
		"""n1Cs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n1Cs'):
			from .N1Cs import N1Cs
			self._n1Cs = N1Cs(self._core, self._cmd_group)
		return self._n1Cs

	@property
	def n2Rb(self):
		"""n2Rb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_n2Rb'):
			from .N2Rb import N2Rb
			self._n2Rb = N2Rb(self._core, self._cmd_group)
		return self._n2Rb

	@property
	def noRb(self):
		"""noRb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noRb'):
			from .NoRb import NoRb
			self._noRb = NoRb(self._core, self._cmd_group)
		return self._noRb

	@property
	def npar(self):
		"""npar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npar'):
			from .Npar import Npar
			self._npar = Npar(self._core, self._cmd_group)
		return self._npar

	@property
	def plid(self):
		"""plid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plid'):
			from .Plid import Plid
			self._plid = Plid(self._core, self._cmd_group)
		return self._plid

	def clone(self) -> 'Pucch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pucch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
