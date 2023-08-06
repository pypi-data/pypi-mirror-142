from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Load:
	"""Load commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("load", core, parent)

	@property
	def demodSetting(self):
		"""demodSetting commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodSetting'):
			from .DemodSetting import DemodSetting
			self._demodSetting = DemodSetting(self._core, self._cmd_group)
		return self._demodSetting

	@property
	def iq(self):
		"""iq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def settings(self):
		"""settings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def tmodel(self):
		"""tmodel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tmodel'):
			from .Tmodel import Tmodel
			self._tmodel = Tmodel(self._core, self._cmd_group)
		return self._tmodel

	def clone(self) -> 'Load':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Load(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
