from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Next:
	"""Next commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("next", core, parent)

	def set(self) -> None:
		"""SCPI: STATus:QUEue[:NEXT] \n
		Snippet: driver.status.queue.next.set() \n
		This command queries the most recent error queue entry and deletes it. Positive error numbers indicate device-specific
		errors, negative error numbers are error messages defined by SCPI. If the error queue is empty, the error number 0, 'No
		error', is returned. This command is identical to the SYSTem:ERRor[:NEXT]? command. \n
		"""
		self._core.io.write(f'STATus:QUEue:NEXT')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STATus:QUEue[:NEXT] \n
		Snippet: driver.status.queue.next.set_with_opc() \n
		This command queries the most recent error queue entry and deletes it. Positive error numbers indicate device-specific
		errors, negative error numbers are error messages defined by SCPI. If the error queue is empty, the error number 0, 'No
		error', is returned. This command is identical to the SYSTem:ERRor[:NEXT]? command. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STATus:QUEue:NEXT', opc_timeout_ms)
