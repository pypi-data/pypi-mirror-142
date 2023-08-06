from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScData:
	"""ScData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scData", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect:CHANnel[:ITEM]:SCData \n
		Snippet: driver.massMemory.select.channel.item.scData.set(state = False) \n
		This command includes or excludes source calibration data for an optional external generator when storing or loading a
		configuration file. Depending on the used command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...)
		, or only those from the currently selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:CHANnel:ITEM:SCData {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:SELect:CHANnel[:ITEM]:SCData \n
		Snippet: value: bool = driver.massMemory.select.channel.item.scData.get() \n
		This command includes or excludes source calibration data for an optional external generator when storing or loading a
		configuration file. Depending on the used command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...)
		, or only those from the currently selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'MMEMory:SELect:CHANnel:ITEM:SCData?')
		return Conversions.str_to_bool(response)
