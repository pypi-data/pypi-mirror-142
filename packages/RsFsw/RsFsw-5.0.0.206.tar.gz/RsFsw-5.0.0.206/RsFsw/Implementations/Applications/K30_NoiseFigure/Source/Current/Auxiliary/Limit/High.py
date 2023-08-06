from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def get(self) -> float:
		"""SCPI: SOURce:CURRent:AUX:LIMit:HIGH \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.current.auxiliary.limit.high.get() \n
		No command help available \n
			:return: current: No help available"""
		response = self._core.io.query_str(f'SOURce:CURRent:AUX:LIMit:HIGH?')
		return Conversions.str_to_float(response)
