from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Creference:
	"""Creference commands group definition. 7 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("creference", core, parent)

	@property
	def value(self):
		"""value commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_value'):
			from .Value import Value
			self._value = Value(self._core, self._cmd_group)
		return self._value

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def preference(self):
		"""preference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preference'):
			from .Preference import Preference
			self._preference = Preference(self._core, self._cmd_group)
		return self._preference

	@property
	def freference(self):
		"""freference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freference'):
			from .Freference import Freference
			self._freference = Freference(self._core, self._cmd_group)
		return self._freference

	@property
	def harmonics(self):
		"""harmonics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_harmonics'):
			from .Harmonics import Harmonics
			self._harmonics = Harmonics(self._core, self._cmd_group)
		return self._harmonics

	def clone(self) -> 'Creference':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Creference(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
