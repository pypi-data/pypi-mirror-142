from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:TRANsducer:ALL \n
		Snippet: driver.massMemory.select.item.transducer.all.set(state = False) \n
		This command includes or excludes transducer factors when storing or loading a configuration file. Depending on the used
		command, either the items from the entire instrument (MMEMory:SELect[:ITEM]...) , or only those from the currently
		selected channel (MMEM:SELect:CHANnel[:ITEM]...) are stored or loaded. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:ITEM:TRANsducer:ALL {param}')
