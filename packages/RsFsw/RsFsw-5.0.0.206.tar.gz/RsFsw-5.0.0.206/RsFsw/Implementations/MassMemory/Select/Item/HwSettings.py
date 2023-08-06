from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HwSettings:
	"""HwSettings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hwSettings", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:HWSettings \n
		Snippet: driver.massMemory.select.item.hwSettings.set(state = False) \n
		This command includes or excludes measurement (hardware) settings when storing or loading a configuration file.
		Measurement settings include:
			- general channel configuration
			- measurement hardware configuration including markers
			- limit lines Note that a configuration may include no more than 8 limit lines. This number includes active limit lines as well as inactive limit lines that were used last. Therefore the combination of inactivate limit lines depends on the sequence of use with method RsFsw.MassMemory.Load.State.set.
			- color settings
			- configuration for the hardcopy output
		Depending on the used command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those
		from the currently selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:ITEM:HWSettings {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:SELect[:ITEM]:HWSettings \n
		Snippet: value: bool = driver.massMemory.select.item.hwSettings.get() \n
		This command includes or excludes measurement (hardware) settings when storing or loading a configuration file.
		Measurement settings include:
			- general channel configuration
			- measurement hardware configuration including markers
			- limit lines Note that a configuration may include no more than 8 limit lines. This number includes active limit lines as well as inactive limit lines that were used last. Therefore the combination of inactivate limit lines depends on the sequence of use with method RsFsw.MassMemory.Load.State.set.
			- color settings
			- configuration for the hardcopy output
		Depending on the used command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those
		from the currently selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'MMEMory:SELect:ITEM:HWSettings?')
		return Conversions.str_to_bool(response)
