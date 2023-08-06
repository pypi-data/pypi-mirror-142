from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> List[str]:
		"""SCPI: SYSTem:ERRor:ALL \n
		Snippet: value: List[str] = driver.system.error.all.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SYSTem:ERRor:ALL?')
		return Conversions.str_to_str_list(response)
