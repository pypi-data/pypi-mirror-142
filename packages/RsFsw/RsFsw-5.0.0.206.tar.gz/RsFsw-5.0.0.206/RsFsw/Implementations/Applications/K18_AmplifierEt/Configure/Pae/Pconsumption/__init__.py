from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconsumption:
	"""Pconsumption commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pconsumption", core, parent)

	@property
	def parameter(self):
		"""parameter commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_parameter'):
			from .Parameter import Parameter
			self._parameter = Parameter(self._core, self._cmd_group)
		return self._parameter

	def clone(self) -> 'Pconsumption':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pconsumption(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
