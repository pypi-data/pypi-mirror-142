from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 7 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import Center
			self._center = Center(self._core, self._cmd_group)
		return self._center

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	@property
	def stop(self):
		"""stop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stop'):
			from .Stop import Stop
			self._stop = Stop(self._core, self._cmd_group)
		return self._stop

	@property
	def verify(self):
		"""verify commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_verify'):
			from .Verify import Verify
			self._verify = Verify(self._core, self._cmd_group)
		return self._verify

	@property
	def track(self):
		"""track commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_track'):
			from .Track import Track
			self._track = Track(self._core, self._cmd_group)
		return self._track

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
