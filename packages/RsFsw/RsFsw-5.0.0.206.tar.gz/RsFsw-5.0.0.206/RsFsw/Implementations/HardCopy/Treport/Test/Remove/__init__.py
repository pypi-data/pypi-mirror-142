from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remove:
	"""Remove commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remove", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def selected(self):
		"""selected commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selected'):
			from .Selected import Selected
			self._selected = Selected(self._core, self._cmd_group)
		return self._selected

	def set(self, arg_0: float) -> None:
		"""SCPI: HCOPy:TREPort:TEST:REMove \n
		Snippet: driver.hardCopy.treport.test.remove.set(arg_0 = 1.0) \n
		This command deletes one of the datasets that are currently part of a test report. \n
			:param arg_0: Index number of the dataset as shown in the 'Test Report Content Selection' dialog box. If the index number is greater than the number of available datasets, the command returns an error.
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'HCOPy:TREPort:TEST:REMove {param}')

	def clone(self) -> 'Remove':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Remove(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
