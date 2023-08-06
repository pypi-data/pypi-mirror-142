from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self) -> List[str]:
		"""SCPI: SYSTem:OPTion:TRIal:LIST \n
		Snippet: value: List[str] = driver.system.option.trial.listPy.get() \n
		Queries availability of applications using trial option T0. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SYSTem:OPTion:TRIal:LIST?')
		return Conversions.str_to_str_list(response)
