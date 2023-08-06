from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fetch:
	"""Fetch commands group definition. 485 total commands, 20 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fetch", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def mdpd(self):
		"""mdpd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdpd'):
			from .Mdpd import Mdpd
			self._mdpd = Mdpd(self._core, self._cmd_group)
		return self._mdpd

	@property
	def power(self):
		"""power commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def amam(self):
		"""amam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import Amam
			self._amam = Amam(self._core, self._cmd_group)
		return self._amam

	@property
	def amPm(self):
		"""amPm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPm
			self._amPm = AmPm(self._core, self._cmd_group)
		return self._amPm

	@property
	def apae(self):
		"""apae commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apae'):
			from .Apae import Apae
			self._apae = Apae(self._core, self._cmd_group)
		return self._apae

	@property
	def bbPower(self):
		"""bbPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbPower'):
			from .BbPower import BbPower
			self._bbPower = BbPower(self._core, self._cmd_group)
		return self._bbPower

	@property
	def dpd(self):
		"""dpd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpd'):
			from .Dpd import Dpd
			self._dpd = Dpd(self._core, self._cmd_group)
		return self._dpd

	@property
	def ddpd(self):
		"""ddpd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ddpd'):
			from .Ddpd import Ddpd
			self._ddpd = Ddpd(self._core, self._cmd_group)
		return self._ddpd

	@property
	def icc(self):
		"""icc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_icc'):
			from .Icc import Icc
			self._icc = Icc(self._core, self._cmd_group)
		return self._icc

	@property
	def ivoltage(self):
		"""ivoltage commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ivoltage'):
			from .Ivoltage import Ivoltage
			self._ivoltage = Ivoltage(self._core, self._cmd_group)
		return self._ivoltage

	@property
	def maccuracy(self):
		"""maccuracy commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_maccuracy'):
			from .Maccuracy import Maccuracy
			self._maccuracy = Maccuracy(self._core, self._cmd_group)
		return self._maccuracy

	@property
	def pc(self):
		"""pc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pc'):
			from .Pc import Pc
			self._pc = Pc(self._core, self._cmd_group)
		return self._pc

	@property
	def pcpa(self):
		"""pcpa commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcpa'):
			from .Pcpa import Pcpa
			self._pcpa = Pcpa(self._core, self._cmd_group)
		return self._pcpa

	@property
	def ptable(self):
		"""ptable commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptable'):
			from .Ptable import Ptable
			self._ptable = Ptable(self._core, self._cmd_group)
		return self._ptable

	@property
	def qvoltage(self):
		"""qvoltage commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qvoltage'):
			from .Qvoltage import Qvoltage
			self._qvoltage = Qvoltage(self._core, self._cmd_group)
		return self._qvoltage

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def ttf(self):
		"""ttf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ttf'):
			from .Ttf import Ttf
			self._ttf = Ttf(self._core, self._cmd_group)
		return self._ttf

	@property
	def tts(self):
		"""tts commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tts'):
			from .Tts import Tts
			self._tts = Tts(self._core, self._cmd_group)
		return self._tts

	@property
	def vcc(self):
		"""vcc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_vcc'):
			from .Vcc import Vcc
			self._vcc = Vcc(self._core, self._cmd_group)
		return self._vcc

	@property
	def stable(self):
		"""stable commands group. 27 Sub-classes, 0 commands."""
		if not hasattr(self, '_stable'):
			from .Stable import Stable
			self._stable = Stable(self._core, self._cmd_group)
		return self._stable

	def clone(self) -> 'Fetch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fetch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
