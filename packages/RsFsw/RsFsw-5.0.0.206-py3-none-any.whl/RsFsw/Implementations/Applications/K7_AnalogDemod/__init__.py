from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K7_AnalogDemod:
	"""K7_AnalogDemod commands group definition. 4 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k7_AnalogDemod", core, parent)

	@property
	def layout(self):
		"""layout commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_layout'):
			from .Layout import Layout
			self._layout = Layout(self._core, self._cmd_group)
		return self._layout

	def clone(self) -> 'K7_AnalogDemod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = K7_AnalogDemod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
