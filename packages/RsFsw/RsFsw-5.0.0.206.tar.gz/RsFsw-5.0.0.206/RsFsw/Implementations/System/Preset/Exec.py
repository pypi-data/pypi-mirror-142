from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Exec:
	"""Exec commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("exec", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:PRESet[:EXEC] \n
		Snippet: driver.system.preset.exec.set() \n
		This command presets the R&S FSW. It is identical to *RST. \n
		"""
		self._core.io.write(f'SYSTem:PRESet:EXEC')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PRESet[:EXEC] \n
		Snippet: driver.system.preset.exec.set_with_opc() \n
		This command presets the R&S FSW. It is identical to *RST. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PRESet:EXEC', opc_timeout_ms)
