from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Remote:
	"""Remote commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("remote", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:ERRor:CLEar:REMote \n
		Snippet: driver.system.error.clear.remote.set() \n
		This command deletes all contents of the 'Remote Errors' table. Note: The remote error list is automatically cleared when
		the R&S FSW is shut down. \n
		"""
		self._core.io.write(f'SYSTem:ERRor:CLEar:REMote')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:ERRor:CLEar:REMote \n
		Snippet: driver.system.error.clear.remote.set_with_opc() \n
		This command deletes all contents of the 'Remote Errors' table. Note: The remote error list is automatically cleared when
		the R&S FSW is shut down. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:ERRor:CLEar:REMote', opc_timeout_ms)
