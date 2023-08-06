from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: SOURce:CURRent:SEQuence:RESult \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.current.sequence.result.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SOURce:CURRent:SEQuence:RESult?')
		return Conversions.str_to_float(response)
