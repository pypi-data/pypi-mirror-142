from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LanReset:
	"""LanReset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lanReset", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:LXI:LANReset \n
		Snippet: driver.system.lxi.lanReset.set() \n
		This command resets the LAN configuration, as well as the 'LAN' password and instrument description. \n
		"""
		self._core.io.write(f'SYSTem:LXI:LANReset')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:LXI:LANReset \n
		Snippet: driver.system.lxi.lanReset.set_with_opc() \n
		This command resets the LAN configuration, as well as the 'LAN' password and instrument description. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:LXI:LANReset', opc_timeout_ms)
