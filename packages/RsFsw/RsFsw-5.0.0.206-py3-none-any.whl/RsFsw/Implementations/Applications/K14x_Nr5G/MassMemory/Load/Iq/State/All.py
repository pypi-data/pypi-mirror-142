from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, state: List[int]) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe:ALL \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.iq.state.all.set(state = [1, 2, 3]) \n
		This command restores the captured I/Q data of all measurements in a combined measurement sequence to a file. The file
		extension is *.iq.tar. \n
			:param state: String containing the path and name of the target file.
		"""
		param = Conversions.list_to_csv_str(state)
		self._core.io.write(f'MMEMory:LOAD:IQ:STATe:ALL {param}')

	def get(self) -> List[int]:
		"""SCPI: MMEMory:LOAD:IQ:STATe:ALL \n
		Snippet: value: List[int] = driver.applications.k14Xnr5G.massMemory.load.iq.state.all.get() \n
		This command restores the captured I/Q data of all measurements in a combined measurement sequence to a file. The file
		extension is *.iq.tar. \n
			:return: state: No help available"""
		response = self._core.io.query_bin_or_ascii_int_list(f'MMEMory:LOAD:IQ:STATe:ALL?')
		return response
