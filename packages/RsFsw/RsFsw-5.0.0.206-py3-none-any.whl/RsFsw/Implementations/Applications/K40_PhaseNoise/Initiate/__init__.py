from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Initiate:
	"""Initiate commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("initiate", core, parent)

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import Immediate
			self._immediate = Immediate(self._core, self._cmd_group)
		return self._immediate

	@property
	def conMeas(self):
		"""conMeas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conMeas'):
			from .ConMeas import ConMeas
			self._conMeas = ConMeas(self._core, self._cmd_group)
		return self._conMeas

	@property
	def continuous(self):
		"""continuous commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_continuous'):
			from .Continuous import Continuous
			self._continuous = Continuous(self._core, self._cmd_group)
		return self._continuous

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	def clone(self) -> 'Initiate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Initiate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
