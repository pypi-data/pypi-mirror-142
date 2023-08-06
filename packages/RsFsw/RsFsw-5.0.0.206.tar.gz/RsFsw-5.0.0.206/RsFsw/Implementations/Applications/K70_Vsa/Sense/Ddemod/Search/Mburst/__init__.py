from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mburst:
	"""Mburst commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mburst", core, parent)

	@property
	def calc(self):
		"""calc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_calc'):
			from .Calc import Calc
			self._calc = Calc(self._core, self._cmd_group)
		return self._calc

	@property
	def start(self):
		"""start commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	def clone(self) -> 'Mburst':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mburst(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
