from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, file: List[int]) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.applications.k10Xlte.massMemory.load.iq.state.set(file = [1, 2, 3]) \n
		This command restores I/Q data from a file. \n
			:param file: String containing the path and name of the source file.
		"""
		param = Conversions.list_to_csv_str(file)
		self._core.io.write(f'MMEMory:LOAD:IQ:STATe {param}')
