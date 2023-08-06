from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Error:
	"""Error commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("error", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def clear(self):
		"""clear commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import Clear
			self._clear = Clear(self._core, self._cmd_group)
		return self._clear

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	def clear_all(self) -> None:
		"""SCPI: SYSTem:ERRor:CLEar:ALL \n
		Snippet: driver.system.error.clear_all() \n
		This command deletes all contents of the 'System Messages' table. \n
		"""
		self._core.io.write(f'SYSTem:ERRor:CLEar:ALL')

	def clear_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:ERRor:CLEar:ALL \n
		Snippet: driver.system.error.clear_all_with_opc() \n
		This command deletes all contents of the 'System Messages' table. \n
		Same as clear_all, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:ERRor:CLEar:ALL', opc_timeout_ms)

	def clone(self) -> 'Error':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Error(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
