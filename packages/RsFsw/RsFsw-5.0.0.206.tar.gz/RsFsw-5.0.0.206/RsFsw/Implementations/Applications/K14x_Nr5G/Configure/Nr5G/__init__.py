from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5G:
	"""Nr5G commands group definition. 349 total commands, 27 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	@property
	def aclr(self):
		"""aclr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import Aclr
			self._aclr = Aclr(self._core, self._cmd_group)
		return self._aclr

	@property
	def bstation(self):
		"""bstation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bstation'):
			from .Bstation import Bstation
			self._bstation = Bstation(self._core, self._cmd_group)
		return self._bstation

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import Center
			self._center = Center(self._core, self._cmd_group)
		return self._center

	@property
	def craster(self):
		"""craster commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_craster'):
			from .Craster import Craster
			self._craster = Craster(self._core, self._cmd_group)
		return self._craster

	@property
	def cspacing(self):
		"""cspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cspacing'):
			from .Cspacing import Cspacing
			self._cspacing = Cspacing(self._core, self._cmd_group)
		return self._cspacing

	@property
	def csCapture(self):
		"""csCapture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csCapture'):
			from .CsCapture import CsCapture
			self._csCapture = CsCapture(self._core, self._cmd_group)
		return self._csCapture

	@property
	def evm(self):
		"""evm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def fcOffset(self):
		"""fcOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcOffset'):
			from .FcOffset import FcOffset
			self._fcOffset = FcOffset(self._core, self._cmd_group)
		return self._fcOffset

	@property
	def felc(self):
		"""felc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_felc'):
			from .Felc import Felc
			self._felc = Felc(self._core, self._cmd_group)
		return self._felc

	@property
	def gmcFreq(self):
		"""gmcFreq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gmcFreq'):
			from .GmcFreq import GmcFreq
			self._gmcFreq = GmcFreq(self._core, self._cmd_group)
		return self._gmcFreq

	@property
	def sem(self):
		"""sem commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sem'):
			from .Sem import Sem
			self._sem = Sem(self._core, self._cmd_group)
		return self._sem

	@property
	def downlink(self):
		"""downlink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def ldirection(self):
		"""ldirection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldirection'):
			from .Ldirection import Ldirection
			self._ldirection = Ldirection(self._core, self._cmd_group)
		return self._ldirection

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	@property
	def msHelper(self):
		"""msHelper commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_msHelper'):
			from .MsHelper import MsHelper
			self._msHelper = MsHelper(self._core, self._cmd_group)
		return self._msHelper

	@property
	def ncSpacing(self):
		"""ncSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncSpacing'):
			from .NcSpacing import NcSpacing
			self._ncSpacing = NcSpacing(self._core, self._cmd_group)
		return self._ncSpacing

	@property
	def noCc(self):
		"""noCc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noCc'):
			from .NoCc import NoCc
			self._noCc = NoCc(self._core, self._cmd_group)
		return self._noCc

	@property
	def nrqMaster(self):
		"""nrqMaster commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrqMaster'):
			from .NrqMaster import NrqMaster
			self._nrqMaster = NrqMaster(self._core, self._cmd_group)
		return self._nrqMaster

	@property
	def nrqPrimary(self):
		"""nrqPrimary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrqPrimary'):
			from .NrqPrimary import NrqPrimary
			self._nrqPrimary = NrqPrimary(self._core, self._cmd_group)
		return self._nrqPrimary

	@property
	def nsources(self):
		"""nsources commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsources'):
			from .Nsources import Nsources
			self._nsources = Nsources(self._core, self._cmd_group)
		return self._nsources

	@property
	def oband(self):
		"""oband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oband'):
			from .Oband import Oband
			self._oband = Oband(self._core, self._cmd_group)
		return self._oband

	@property
	def omode(self):
		"""omode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_omode'):
			from .Omode import Omode
			self._omode = Omode(self._core, self._cmd_group)
		return self._omode

	@property
	def orel(self):
		"""orel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_orel'):
			from .Orel import Orel
			self._orel = Orel(self._core, self._cmd_group)
		return self._orel

	@property
	def ooPower(self):
		"""ooPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPower
			self._ooPower = OoPower(self._core, self._cmd_group)
		return self._ooPower

	@property
	def oran(self):
		"""oran commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_oran'):
			from .Oran import Oran
			self._oran = Oran(self._core, self._cmd_group)
		return self._oran

	@property
	def simulation(self):
		"""simulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_simulation'):
			from .Simulation import Simulation
			self._simulation = Simulation(self._core, self._cmd_group)
		return self._simulation

	@property
	def uplink(self):
		"""uplink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'Nr5G':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr5G(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
