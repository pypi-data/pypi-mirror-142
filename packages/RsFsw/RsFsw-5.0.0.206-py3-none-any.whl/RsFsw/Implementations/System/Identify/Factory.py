from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factory:
	"""Factory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factory", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:IDENtify:FACTory \n
		Snippet: driver.system.identify.factory.set() \n
		This command resets the query to *IDN? to its default value. \n
		"""
		self._core.io.write(f'SYSTem:IDENtify:FACTory')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:IDENtify:FACTory \n
		Snippet: driver.system.identify.factory.set_with_opc() \n
		This command resets the query to *IDN? to its default value. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:IDENtify:FACTory', opc_timeout_ms)
