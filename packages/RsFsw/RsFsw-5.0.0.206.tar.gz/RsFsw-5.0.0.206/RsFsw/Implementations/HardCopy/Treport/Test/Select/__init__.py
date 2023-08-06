from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def nonePy(self):
		"""nonePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nonePy'):
			from .NonePy import NonePy
			self._nonePy = NonePy(self._core, self._cmd_group)
		return self._nonePy

	@property
	def invert(self):
		"""invert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_invert'):
			from .Invert import Invert
			self._invert = Invert(self._core, self._cmd_group)
		return self._invert

	def set(self, arg_0: float, arg_1: bool) -> None:
		"""SCPI: HCOPy:TREPort:TEST:SELect \n
		Snippet: driver.hardCopy.treport.test.select.set(arg_0 = 1.0, arg_1 = False) \n
		No command help available \n
			:param arg_0: No help available
			:param arg_1: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Float), ArgSingle('arg_1', arg_1, DataType.Boolean))
		self._core.io.write(f'HCOPy:TREPort:TEST:SELect {param}'.rstrip())

	def clone(self) -> 'Select':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Select(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
