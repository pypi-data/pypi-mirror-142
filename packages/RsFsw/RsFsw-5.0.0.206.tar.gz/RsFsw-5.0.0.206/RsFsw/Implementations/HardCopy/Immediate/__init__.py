from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	@property
	def next(self):
		"""next commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_next'):
			from .Next import Next
			self._next = Next(self._core, self._cmd_group)
		return self._next

	def set(self) -> None:
		"""SCPI: HCOPy[:IMMediate] \n
		Snippet: driver.hardCopy.immediate.set() \n
		This command initiates a print job. If you are printing to a file, the file name depends on method RsFsw.MassMemory.Name.
		set. \n
		"""
		self._core.io.write(f'HCOPy:IMMediate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy[:IMMediate] \n
		Snippet: driver.hardCopy.immediate.set_with_opc() \n
		This command initiates a print job. If you are printing to a file, the file name depends on method RsFsw.MassMemory.Name.
		set. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:IMMediate', opc_timeout_ms)

	def clone(self) -> 'Immediate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Immediate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
