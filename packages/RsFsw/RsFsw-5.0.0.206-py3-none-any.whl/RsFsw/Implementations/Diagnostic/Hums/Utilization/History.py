from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class History:
	"""History commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("history", core, parent)

	def get(self) -> bytes:
		"""SCPI: DIAGnostic:HUMS:UTILization:HISTory \n
		Snippet: value: bytes = driver.diagnostic.hums.utilization.history.get() \n
		No command help available \n
			:return: util_history: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:HUMS:UTILization:HISTory?')
		return response

	def delete_all(self) -> None:
		"""SCPI: DIAGnostic:HUMS:UTILization:HISTory:DELete:ALL \n
		Snippet: driver.diagnostic.hums.utilization.history.delete_all() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic:HUMS:UTILization:HISTory:DELete:ALL')

	def delete_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic:HUMS:UTILization:HISTory:DELete:ALL \n
		Snippet: driver.diagnostic.hums.utilization.history.delete_all_with_opc() \n
		No command help available \n
		Same as delete_all, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic:HUMS:UTILization:HISTory:DELete:ALL', opc_timeout_ms)
