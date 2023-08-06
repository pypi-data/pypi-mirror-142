from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self) -> List[str]:
		"""SCPI: [SENSe]:CORRection:LOSS:CALibration:TABLe:LIST \n
		Snippet: value: List[str] = driver.applications.k30NoiseFigure.sense.correction.loss.calibration.table.listPy.get() \n
		This command queries all calibration loss tables available in the application. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SENSe:CORRection:LOSS:CALibration:TABLe:LIST?')
		return Conversions.str_to_str_list(response)
