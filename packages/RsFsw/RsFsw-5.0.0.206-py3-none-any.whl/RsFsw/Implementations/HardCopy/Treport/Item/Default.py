from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	def set(self) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:DEFault \n
		Snippet: driver.hardCopy.treport.item.default.set() \n
		No command help available \n
		"""
		self._core.io.write(f'HCOPy:TREPort:ITEM:DEFault')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:DEFault \n
		Snippet: driver.hardCopy.treport.item.default.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:TREPort:ITEM:DEFault', opc_timeout_ms)
