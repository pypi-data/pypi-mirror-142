from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cwf:
	"""Cwf commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cwf", core, parent)

	@property
	def dpiPower(self):
		"""dpiPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpiPower'):
			from .DpiPower import DpiPower
			self._dpiPower = DpiPower(self._core, self._cmd_group)
		return self._dpiPower

	@property
	def etGenerator(self):
		"""etGenerator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_etGenerator'):
			from .EtGenerator import EtGenerator
			self._etGenerator = EtGenerator(self._core, self._cmd_group)
		return self._etGenerator

	@property
	def fpath(self):
		"""fpath commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpath'):
			from .Fpath import Fpath
			self._fpath = Fpath(self._core, self._cmd_group)
		return self._fpath

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	@property
	def write(self):
		"""write commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_write'):
			from .Write import Write
			self._write = Write(self._core, self._cmd_group)
		return self._write

	def clone(self) -> 'Cwf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cwf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
