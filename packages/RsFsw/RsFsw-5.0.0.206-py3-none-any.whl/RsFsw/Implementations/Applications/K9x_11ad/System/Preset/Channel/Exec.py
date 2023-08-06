from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Exec:
	"""Exec commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("exec", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:PRESet:CHANnel[:EXEC] \n
		Snippet: driver.applications.k9X11Ad.system.preset.channel.exec.set() \n
		This command restores the default instrument settings in the current channel. Use INST:SEL to select the channel. \n
		"""
		self._core.io.write(f'SYSTem:PRESet:CHANnel:EXEC')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PRESet:CHANnel[:EXEC] \n
		Snippet: driver.applications.k9X11Ad.system.preset.channel.exec.set_with_opc() \n
		This command restores the default instrument settings in the current channel. Use INST:SEL to select the channel. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PRESet:CHANnel:EXEC', opc_timeout_ms)
