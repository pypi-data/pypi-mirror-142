from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self) -> None:
		"""SCPI: INITiate[:IMMediate] \n
		Snippet: driver.applications.k60Transient.initiate.immediate.set() \n
		This command starts a (single) new measurement. You can synchronize to the end of the measurement with *OPC, *OPC?
		or *WAI. For details on synchronization see Remote control via SCPI. \n
		"""
		self._core.io.write(f'INITiate:IMMediate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate[:IMMediate] \n
		Snippet: driver.applications.k60Transient.initiate.immediate.set_with_opc() \n
		This command starts a (single) new measurement. You can synchronize to the end of the measurement with *OPC, *OPC?
		or *WAI. For details on synchronization see Remote control via SCPI. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:IMMediate', opc_timeout_ms)
