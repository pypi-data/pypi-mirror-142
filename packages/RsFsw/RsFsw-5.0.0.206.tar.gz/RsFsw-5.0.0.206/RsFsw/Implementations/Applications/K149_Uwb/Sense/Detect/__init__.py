from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detect:
	"""Detect commands group definition. 7 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detect", core, parent)

	@property
	def burst(self):
		"""burst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	@property
	def default(self):
		"""default commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_default'):
			from .Default import Default
			self._default = Default(self._core, self._cmd_group)
		return self._default

	@property
	def evaluation(self):
		"""evaluation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_evaluation'):
			from .Evaluation import Evaluation
			self._evaluation = Evaluation(self._core, self._cmd_group)
		return self._evaluation

	@property
	def off(self):
		"""off commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_off'):
			from .Off import Off
			self._off = Off(self._core, self._cmd_group)
		return self._off

	@property
	def reference(self):
		"""reference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	@property
	def threshold(self):
		"""threshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_threshold'):
			from .Threshold import Threshold
			self._threshold = Threshold(self._core, self._cmd_group)
		return self._threshold

	def clone(self) -> 'Detect':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Detect(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
