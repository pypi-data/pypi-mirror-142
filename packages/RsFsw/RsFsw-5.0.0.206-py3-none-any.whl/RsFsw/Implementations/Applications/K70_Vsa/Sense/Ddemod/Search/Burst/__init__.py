from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Burst:
	"""Burst commands group definition. 10 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("burst", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tolerance(self):
		"""tolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tolerance'):
			from .Tolerance import Tolerance
			self._tolerance = Tolerance(self._core, self._cmd_group)
		return self._tolerance

	@property
	def glength(self):
		"""glength commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_glength'):
			from .Glength import Glength
			self._glength = Glength(self._core, self._cmd_group)
		return self._glength

	@property
	def length(self):
		"""length commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	@property
	def skip(self):
		"""skip commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_skip'):
			from .Skip import Skip
			self._skip = Skip(self._core, self._cmd_group)
		return self._skip

	@property
	def configure(self):
		"""configure commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import Configure
			self._configure = Configure(self._core, self._cmd_group)
		return self._configure

	def clone(self) -> 'Burst':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Burst(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
