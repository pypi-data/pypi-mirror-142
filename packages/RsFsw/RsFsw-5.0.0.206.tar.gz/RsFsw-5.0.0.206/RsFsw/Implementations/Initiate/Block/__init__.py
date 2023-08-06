from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Block:
	"""Block commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("block", core, parent)

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

	def abort(self) -> None:
		"""SCPI: INITiate:BLOCk:ABORt \n
		Snippet: driver.initiate.block.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:BLOCk:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:BLOCk:ABORt \n
		Snippet: driver.initiate.block.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:BLOCk:ABORt', opc_timeout_ms)

	def clone(self) -> 'Block':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Block(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
