from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: INITiate:SEQuencer:REFResh[:ALL] \n
		Snippet: driver.initiate.sequencer.refresh.all.set() \n
		This function is only available if the Sequencer is deactivated (SYST:SEQ:OFF) and only in MSRT mode. The data in the
		capture buffer is re-evaluated by all active MSRT secondary applications. \n
		"""
		self._core.io.write(f'INITiate:SEQuencer:REFResh:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:SEQuencer:REFResh[:ALL] \n
		Snippet: driver.initiate.sequencer.refresh.all.set_with_opc() \n
		This function is only available if the Sequencer is deactivated (SYST:SEQ:OFF) and only in MSRT mode. The data in the
		capture buffer is re-evaluated by all active MSRT secondary applications. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:SEQuencer:REFResh:ALL', opc_timeout_ms)
