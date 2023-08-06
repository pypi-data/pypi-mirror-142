from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:CMEasurement:PNDB[:RESult] \n
		Snippet: value: float = driver.fetch.cmeasurement.pndb.result.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:CMEasurement:PNDB:RESult?')
		return Conversions.str_to_float(response)
