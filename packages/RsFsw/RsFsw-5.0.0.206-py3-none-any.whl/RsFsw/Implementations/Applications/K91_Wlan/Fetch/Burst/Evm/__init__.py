from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 15 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def ieee(self):
		"""ieee commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ieee'):
			from .Ieee import Ieee
			self._ieee = Ieee(self._core, self._cmd_group)
		return self._ieee

	@property
	def direct(self):
		"""direct commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_direct'):
			from .Direct import Direct
			self._direct = Direct(self._core, self._cmd_group)
		return self._direct

	@property
	def all(self):
		"""all commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def data(self):
		"""data commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def pilot(self):
		"""pilot commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Pilot import Pilot
			self._pilot = Pilot(self._core, self._cmd_group)
		return self._pilot

	def clone(self) -> 'Evm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
