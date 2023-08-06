from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 85 total commands, 29 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	@property
	def iqSkew(self):
		"""iqSkew commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqSkew'):
			from .IqSkew import IqSkew
			self._iqSkew = IqSkew(self._core, self._cmd_group)
		return self._iqSkew

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def am(self):
		"""am commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_am'):
			from .Am import Am
			self._am = Am(self._core, self._cmd_group)
		return self._am

	@property
	def preamble(self):
		"""preamble commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def payload(self):
		"""payload commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_payload'):
			from .Payload import Payload
			self._payload = Payload(self._core, self._cmd_group)
		return self._payload

	@property
	def rms(self):
		"""rms commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import Rms
			self._rms = Rms(self._core, self._cmd_group)
		return self._rms

	@property
	def peak(self):
		"""peak commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def crest(self):
		"""crest commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import Crest
			self._crest = Crest(self._core, self._cmd_group)
		return self._crest

	@property
	def trise(self):
		"""trise commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_trise'):
			from .Trise import Trise
			self._trise = Trise(self._core, self._cmd_group)
		return self._trise

	@property
	def tfall(self):
		"""tfall commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tfall'):
			from .Tfall import Tfall
			self._tfall = Tfall(self._core, self._cmd_group)
		return self._tfall

	@property
	def freqError(self):
		"""freqError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqError
			self._freqError = FreqError(self._core, self._cmd_group)
		return self._freqError

	@property
	def symbolError(self):
		"""symbolError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbolError'):
			from .SymbolError import SymbolError
			self._symbolError = SymbolError(self._core, self._cmd_group)
		return self._symbolError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def quadOffset(self):
		"""quadOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadOffset'):
			from .QuadOffset import QuadOffset
			self._quadOffset = QuadOffset(self._core, self._cmd_group)
		return self._quadOffset

	@property
	def berPilot(self):
		"""berPilot commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_berPilot'):
			from .BerPilot import BerPilot
			self._berPilot = BerPilot(self._core, self._cmd_group)
		return self._berPilot

	@property
	def mcPower(self):
		"""mcPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcPower'):
			from .McPower import McPower
			self._mcPower = McPower(self._core, self._cmd_group)
		return self._mcPower

	@property
	def mchPower(self):
		"""mchPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mchPower'):
			from .MchPower import MchPower
			self._mchPower = MchPower(self._core, self._cmd_group)
		return self._mchPower

	@property
	def cfError(self):
		"""cfError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfError
			self._cfError = CfError(self._core, self._cmd_group)
		return self._cfError

	@property
	def cpError(self):
		"""cpError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cpError'):
			from .CpError import CpError
			self._cpError = CpError(self._core, self._cmd_group)
		return self._cpError

	@property
	def evm(self):
		"""evm commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def ppdu(self):
		"""ppdu commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppdu'):
			from .Ppdu import Ppdu
			self._ppdu = Ppdu(self._core, self._cmd_group)
		return self._ppdu

	@property
	def ecmGain(self):
		"""ecmGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ecmGain'):
			from .EcmGain import EcmGain
			self._ecmGain = EcmGain(self._core, self._cmd_group)
		return self._ecmGain

	@property
	def pcmGain(self):
		"""pcmGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcmGain'):
			from .PcmGain import PcmGain
			self._pcmGain = PcmGain(self._core, self._cmd_group)
		return self._pcmGain

	@property
	def lengths(self):
		"""lengths commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lengths'):
			from .Lengths import Lengths
			self._lengths = Lengths(self._core, self._cmd_group)
		return self._lengths

	@property
	def starts(self):
		"""starts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_starts'):
			from .Starts import Starts
			self._starts = Starts(self._core, self._cmd_group)
		return self._starts

	@property
	def mcsIndex(self):
		"""mcsIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsIndex'):
			from .McsIndex import McsIndex
			self._mcsIndex = McsIndex(self._core, self._cmd_group)
		return self._mcsIndex

	@property
	def ginterval(self):
		"""ginterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ginterval'):
			from .Ginterval import Ginterval
			self._ginterval = Ginterval(self._core, self._cmd_group)
		return self._ginterval

	def clone(self) -> 'Burst':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Burst(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
