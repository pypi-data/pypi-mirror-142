from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: HCOPy:ITEM:ALL \n
		Snippet: driver.hardCopy.item.all.set() \n
		This command is maintained for compatibility reasons only. It has no effect. \n
		"""
		self._core.io.write(f'HCOPy:ITEM:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy:ITEM:ALL \n
		Snippet: driver.hardCopy.item.all.set_with_opc() \n
		This command is maintained for compatibility reasons only. It has no effect. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:ITEM:ALL', opc_timeout_ms)
