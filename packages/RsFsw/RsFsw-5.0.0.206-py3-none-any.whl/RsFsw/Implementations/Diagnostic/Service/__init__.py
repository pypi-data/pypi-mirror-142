from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Service:
	"""Service commands group definition. 29 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("service", core, parent)

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def calibration(self):
		"""calibration commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def inputPy(self):
		"""inputPy commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def sfunction(self):
		"""sfunction commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfunction'):
			from .Sfunction import Sfunction
			self._sfunction = Sfunction(self._core, self._cmd_group)
		return self._sfunction

	@property
	def stest(self):
		"""stest commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_stest'):
			from .Stest import Stest
			self._stest = Stest(self._core, self._cmd_group)
		return self._stest

	@property
	def spCheck(self):
		"""spCheck commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spCheck'):
			from .SpCheck import SpCheck
			self._spCheck = SpCheck(self._core, self._cmd_group)
		return self._spCheck

	@property
	def biosInfo(self):
		"""biosInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_biosInfo'):
			from .BiosInfo import BiosInfo
			self._biosInfo = BiosInfo(self._core, self._cmd_group)
		return self._biosInfo

	@property
	def hwInfo(self):
		"""hwInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hwInfo'):
			from .HwInfo import HwInfo
			self._hwInfo = HwInfo(self._core, self._cmd_group)
		return self._hwInfo

	@property
	def versionInfo(self):
		"""versionInfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_versionInfo'):
			from .VersionInfo import VersionInfo
			self._versionInfo = VersionInfo(self._core, self._cmd_group)
		return self._versionInfo

	@property
	def sinfo(self):
		"""sinfo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import Sinfo
			self._sinfo = Sinfo(self._core, self._cmd_group)
		return self._sinfo

	@property
	def nsource(self):
		"""nsource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsource'):
			from .Nsource import Nsource
			self._nsource = Nsource(self._core, self._cmd_group)
		return self._nsource

	def clone(self) -> 'Service':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Service(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
