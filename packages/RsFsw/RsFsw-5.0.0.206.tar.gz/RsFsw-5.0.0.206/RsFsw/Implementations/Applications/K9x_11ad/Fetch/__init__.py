from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fetch:
	"""Fetch commands group definition. 52 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fetch", core, parent)

	@property
	def evm(self):
		"""evm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def cfactor(self):
		"""cfactor commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def cfError(self):
		"""cfError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfError
			self._cfError = CfError(self._core, self._cmd_group)
		return self._cfError

	@property
	def ftime(self):
		"""ftime commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftime'):
			from .Ftime import Ftime
			self._ftime = Ftime(self._core, self._cmd_group)
		return self._ftime

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def hbeRate(self):
		"""hbeRate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_hbeRate'):
			from .HbeRate import HbeRate
			self._hbeRate = HbeRate(self._core, self._cmd_group)
		return self._hbeRate

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def pbeRate(self):
		"""pbeRate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbeRate'):
			from .PbeRate import PbeRate
			self._pbeRate = PbeRate(self._core, self._cmd_group)
		return self._pbeRate

	@property
	def quadError(self):
		"""quadError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadError'):
			from .QuadError import QuadError
			self._quadError = QuadError(self._core, self._cmd_group)
		return self._quadError

	@property
	def rtime(self):
		"""rtime commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtime'):
			from .Rtime import Rtime
			self._rtime = Rtime(self._core, self._cmd_group)
		return self._rtime

	@property
	def snr(self):
		"""snr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_snr'):
			from .Snr import Snr
			self._snr = Snr(self._core, self._cmd_group)
		return self._snr

	@property
	def symbolError(self):
		"""symbolError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbolError'):
			from .SymbolError import SymbolError
			self._symbolError = SymbolError(self._core, self._cmd_group)
		return self._symbolError

	@property
	def tdPower(self):
		"""tdPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdPower'):
			from .TdPower import TdPower
			self._tdPower = TdPower(self._core, self._cmd_group)
		return self._tdPower

	@property
	def tskew(self):
		"""tskew commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tskew'):
			from .Tskew import Tskew
			self._tskew = Tskew(self._core, self._cmd_group)
		return self._tskew

	@property
	def pmeter(self):
		"""pmeter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def burst(self):
		"""burst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	def clone(self) -> 'Fetch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fetch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
