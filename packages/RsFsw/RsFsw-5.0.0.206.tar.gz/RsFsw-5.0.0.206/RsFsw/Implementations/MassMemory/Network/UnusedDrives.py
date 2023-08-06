from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnusedDrives:
	"""UnusedDrives commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unusedDrives", core, parent)

	def get(self) -> List[str]:
		"""SCPI: MMEMory:NETWork:UNUSeddrives \n
		Snippet: value: List[str] = driver.massMemory.network.unusedDrives.get() \n
		This command returns a list of unused network drives. \n
			:return: drives: No help available"""
		response = self._core.io.query_str_with_opc(f'MMEMory:NETWork:UNUSeddrives?')
		return Conversions.str_to_str_list(response)
