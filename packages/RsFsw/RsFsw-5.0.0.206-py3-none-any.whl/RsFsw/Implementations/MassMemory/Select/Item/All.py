from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:ALL \n
		Snippet: driver.massMemory.select.item.all.set() \n
		This command includes all items when storing or loading a configuration file. Depending on the used command, either the
		items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those from the currently selected channel
		(MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. The items are:
			- Hardware configuration: method RsFsw.MassMemory.Select.Item.HwSettings.set
			- Limit lines: method RsFsw.MassMemory.Select.Item.Lines.All.set
			- Spectrogram data: MMEMory:SELect[:ITEM]:SGRam
			- Trace data: MMEMory:SELect[:ITEM]:TRACe<1...3>[:ACTive]
			- Transducers: method RsFsw.MassMemory.Select.Item.Transducer.All.set \n
		"""
		self._core.io.write(f'MMEMory:SELect:ITEM:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:ALL \n
		Snippet: driver.massMemory.select.item.all.set_with_opc() \n
		This command includes all items when storing or loading a configuration file. Depending on the used command, either the
		items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those from the currently selected channel
		(MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. The items are:
			- Hardware configuration: method RsFsw.MassMemory.Select.Item.HwSettings.set
			- Limit lines: method RsFsw.MassMemory.Select.Item.Lines.All.set
			- Spectrogram data: MMEMory:SELect[:ITEM]:SGRam
			- Trace data: MMEMory:SELect[:ITEM]:TRACe<1...3>[:ACTive]
			- Transducers: method RsFsw.MassMemory.Select.Item.Transducer.All.set \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'MMEMory:SELect:ITEM:ALL', opc_timeout_ms)
