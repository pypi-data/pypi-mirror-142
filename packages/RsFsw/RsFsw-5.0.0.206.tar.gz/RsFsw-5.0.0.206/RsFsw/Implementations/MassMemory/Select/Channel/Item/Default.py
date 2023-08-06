from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)

	def set(self) -> None:
		"""SCPI: MMEMory:SELect:CHANnel[:ITEM]:DEFault \n
		Snippet: driver.massMemory.select.channel.item.default.set() \n
		This command selects the current settings as the only item to store to and load from a configuration file. Depending on
		the used command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those from the
		currently selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
		"""
		self._core.io.write(f'MMEMory:SELect:CHANnel:ITEM:DEFault')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: MMEMory:SELect:CHANnel[:ITEM]:DEFault \n
		Snippet: driver.massMemory.select.channel.item.default.set_with_opc() \n
		This command selects the current settings as the only item to store to and load from a configuration file. Depending on
		the used command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those from the
		currently selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'MMEMory:SELect:CHANnel:ITEM:DEFault', opc_timeout_ms)
