from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fresponse:
	"""Fresponse commands group definition. 89 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fresponse", core, parent)

	@property
	def user(self):
		"""user commands group. 12 Sub-classes, 2 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	@property
	def lsources(self):
		"""lsources commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lsources'):
			from .Lsources import Lsources
			self._lsources = Lsources(self._core, self._cmd_group)
		return self._lsources

	@property
	def baseband(self):
		"""baseband commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_baseband'):
			from .Baseband import Baseband
			self._baseband = Baseband(self._core, self._cmd_group)
		return self._baseband

	@property
	def inputPy(self):
		"""inputPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	def clone(self) -> 'Fresponse':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fresponse(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
