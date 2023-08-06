from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 38 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	@property
	def current(self):
		"""current commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def voltage(self):
		"""voltage commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_voltage'):
			from .Voltage import Voltage
			self._voltage = Voltage(self._core, self._cmd_group)
		return self._voltage

	@property
	def external(self):
		"""external commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	@property
	def nsource(self):
		"""nsource commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nsource'):
			from .Nsource import Nsource
			self._nsource = Nsource(self._core, self._cmd_group)
		return self._nsource

	@property
	def generator(self):
		"""generator commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	def clone(self) -> 'Source':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Source(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
