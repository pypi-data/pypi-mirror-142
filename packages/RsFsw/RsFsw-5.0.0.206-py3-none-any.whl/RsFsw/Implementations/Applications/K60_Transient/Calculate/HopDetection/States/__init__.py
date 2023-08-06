from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class States:
	"""States commands group definition. 12 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("states", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def number(self):
		"""number commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_number'):
			from .Number import Number
			self._number = Number(self._core, self._cmd_group)
		return self._number

	@property
	def table(self):
		"""table commands group. 7 Sub-classes, 2 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	def clone(self) -> 'States':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = States(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
