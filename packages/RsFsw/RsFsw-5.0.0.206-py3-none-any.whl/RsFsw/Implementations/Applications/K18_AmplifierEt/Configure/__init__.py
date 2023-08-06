from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 174 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def cfReduction(self):
		"""cfReduction commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfReduction'):
			from .CfReduction import CfReduction
			self._cfReduction = CfReduction(self._core, self._cmd_group)
		return self._cfReduction

	@property
	def ddpd(self):
		"""ddpd commands group. 10 Sub-classes, 3 commands."""
		if not hasattr(self, '_ddpd'):
			from .Ddpd import Ddpd
			self._ddpd = Ddpd(self._core, self._cmd_group)
		return self._ddpd

	@property
	def dpd(self):
		"""dpd commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpd'):
			from .Dpd import Dpd
			self._dpd = Dpd(self._core, self._cmd_group)
		return self._dpd

	@property
	def dut(self):
		"""dut commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import Dut
			self._dut = Dut(self._core, self._cmd_group)
		return self._dut

	@property
	def equalizer(self):
		"""equalizer commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_equalizer'):
			from .Equalizer import Equalizer
			self._equalizer = Equalizer(self._core, self._cmd_group)
		return self._equalizer

	@property
	def generator(self):
		"""generator commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def frSpan(self):
		"""frSpan commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frSpan'):
			from .FrSpan import FrSpan
			self._frSpan = FrSpan(self._core, self._cmd_group)
		return self._frSpan

	@property
	def modeling(self):
		"""modeling commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_modeling'):
			from .Modeling import Modeling
			self._modeling = Modeling(self._core, self._cmd_group)
		return self._modeling

	@property
	def mdpd(self):
		"""mdpd commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdpd'):
			from .Mdpd import Mdpd
			self._mdpd = Mdpd(self._core, self._cmd_group)
		return self._mdpd

	@property
	def pae(self):
		"""pae commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pae'):
			from .Pae import Pae
			self._pae = Pae(self._core, self._cmd_group)
		return self._pae

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def psweep(self):
		"""psweep commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_psweep'):
			from .Psweep import Psweep
			self._psweep = Psweep(self._core, self._cmd_group)
		return self._psweep

	@property
	def refSignal(self):
		"""refSignal commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_refSignal'):
			from .RefSignal import RefSignal
			self._refSignal = RefSignal(self._core, self._cmd_group)
		return self._refSignal

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def signal(self):
		"""signal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signal'):
			from .Signal import Signal
			self._signal = Signal(self._core, self._cmd_group)
		return self._signal

	@property
	def sync(self):
		"""sync commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
