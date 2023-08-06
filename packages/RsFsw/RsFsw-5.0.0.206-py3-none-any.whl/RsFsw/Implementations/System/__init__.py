from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 91 total commands, 29 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def communicate(self):
		"""communicate commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .Communicate import Communicate
			self._communicate = Communicate(self._core, self._cmd_group)
		return self._communicate

	@property
	def error(self):
		"""error commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_error'):
			from .Error import Error
			self._error = Error(self._core, self._cmd_group)
		return self._error

	@property
	def help(self):
		"""help commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_help'):
			from .Help import Help
			self._help = Help(self._core, self._cmd_group)
		return self._help

	@property
	def speaker(self):
		"""speaker commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_speaker'):
			from .Speaker import Speaker
			self._speaker = Speaker(self._core, self._cmd_group)
		return self._speaker

	@property
	def preset(self):
		"""preset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import Preset
			self._preset = Preset(self._core, self._cmd_group)
		return self._preset

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Set import Set
			self._set = Set(self._core, self._cmd_group)
		return self._set

	@property
	def test(self):
		"""test commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_test'):
			from .Test import Test
			self._test = Test(self._core, self._cmd_group)
		return self._test

	@property
	def identify(self):
		"""identify commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_identify'):
			from .Identify import Identify
			self._identify = Identify(self._core, self._cmd_group)
		return self._identify

	@property
	def revision(self):
		"""revision commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_revision'):
			from .Revision import Revision
			self._revision = Revision(self._core, self._cmd_group)
		return self._revision

	@property
	def display(self):
		"""display commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	@property
	def firmware(self):
		"""firmware commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_firmware'):
			from .Firmware import Firmware
			self._firmware = Firmware(self._core, self._cmd_group)
		return self._firmware

	@property
	def ifGain(self):
		"""ifGain commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifGain'):
			from .IfGain import IfGain
			self._ifGain = IfGain(self._core, self._cmd_group)
		return self._ifGain

	@property
	def language(self):
		"""language commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_language'):
			from .Language import Language
			self._language = Language(self._core, self._cmd_group)
		return self._language

	@property
	def plugin(self):
		"""plugin commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_plugin'):
			from .Plugin import Plugin
			self._plugin = Plugin(self._core, self._cmd_group)
		return self._plugin

	@property
	def psa(self):
		"""psa commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psa'):
			from .Psa import Psa
			self._psa = Psa(self._core, self._cmd_group)
		return self._psa

	@property
	def preamp(self):
		"""preamp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamp'):
			from .Preamp import Preamp
			self._preamp = Preamp(self._core, self._cmd_group)
		return self._preamp

	@property
	def rsweep(self):
		"""rsweep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsweep'):
			from .Rsweep import Rsweep
			self._rsweep = Rsweep(self._core, self._cmd_group)
		return self._rsweep

	@property
	def formatPy(self):
		"""formatPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def compatible(self):
		"""compatible commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_compatible'):
			from .Compatible import Compatible
			self._compatible = Compatible(self._core, self._cmd_group)
		return self._compatible

	@property
	def clogging(self):
		"""clogging commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clogging'):
			from .Clogging import Clogging
			self._clogging = Clogging(self._core, self._cmd_group)
		return self._clogging

	@property
	def shutdown(self):
		"""shutdown commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shutdown'):
			from .Shutdown import Shutdown
			self._shutdown = Shutdown(self._core, self._cmd_group)
		return self._shutdown

	@property
	def reboot(self):
		"""reboot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reboot'):
			from .Reboot import Reboot
			self._reboot = Reboot(self._core, self._cmd_group)
		return self._reboot

	@property
	def osystem(self):
		"""osystem commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_osystem'):
			from .Osystem import Osystem
			self._osystem = Osystem(self._core, self._cmd_group)
		return self._osystem

	@property
	def deviceFootprint(self):
		"""deviceFootprint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviceFootprint'):
			from .DeviceFootprint import DeviceFootprint
			self._deviceFootprint = DeviceFootprint(self._core, self._cmd_group)
		return self._deviceFootprint

	@property
	def lxi(self):
		"""lxi commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_lxi'):
			from .Lxi import Lxi
			self._lxi = Lxi(self._core, self._cmd_group)
		return self._lxi

	@property
	def sequencer(self):
		"""sequencer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._cmd_group)
		return self._sequencer

	@property
	def security(self):
		"""security commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_security'):
			from .Security import Security
			self._security = Security(self._core, self._cmd_group)
		return self._security

	@property
	def shImmediate(self):
		"""shImmediate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_shImmediate'):
			from .ShImmediate import ShImmediate
			self._shImmediate = ShImmediate(self._core, self._cmd_group)
		return self._shImmediate

	@property
	def option(self):
		"""option commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_option'):
			from .Option import Option
			self._option = Option(self._core, self._cmd_group)
		return self._option

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
