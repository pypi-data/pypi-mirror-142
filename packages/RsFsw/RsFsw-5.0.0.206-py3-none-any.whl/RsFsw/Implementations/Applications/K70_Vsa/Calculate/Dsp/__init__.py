from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dsp:
	"""Dsp commands group definition. 9 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsp", core, parent)

	@property
	def result(self):
		"""result commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	def clone(self) -> 'Dsp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dsp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
