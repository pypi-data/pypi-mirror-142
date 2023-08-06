from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 32 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	@property
	def am(self):
		"""am commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_am'):
			from .Am import Am
			self._am = Am(self._core, self._cmd_group)
		return self._am

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def preamble(self):
		"""preamble commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def ptracking(self):
		"""ptracking commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptracking'):
			from .Ptracking import Ptracking
			self._ptracking = Ptracking(self._core, self._cmd_group)
		return self._ptracking

	@property
	def pvt(self):
		"""pvt commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pvt'):
			from .Pvt import Pvt
			self._pvt = Pvt(self._core, self._cmd_group)
		return self._pvt

	@property
	def evm(self):
		"""evm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def gain(self):
		"""gain commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def quad(self):
		"""quad commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_quad'):
			from .Quad import Quad
			self._quad = Quad(self._core, self._cmd_group)
		return self._quad

	@property
	def spectrum(self):
		"""spectrum commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def const(self):
		"""const commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_const'):
			from .Const import Const
			self._const = Const(self._core, self._cmd_group)
		return self._const

	@property
	def statistics(self):
		"""statistics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import Statistics
			self._statistics = Statistics(self._core, self._cmd_group)
		return self._statistics

	def clone(self) -> 'Burst':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Burst(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
