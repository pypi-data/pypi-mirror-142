from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self, error: enums.SelectionRangeB) -> float:
		"""SCPI: FETCh:STABle:FERRor:AVERage \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.stable.freqError.average.get(error = enums.SelectionRangeB.ALL) \n
		No command help available \n
			:param error: No help available
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(error, enums.SelectionRangeB)
		response = self._core.io.query_str(f'FETCh:STABle:FERRor:AVERage? {param}')
		return Conversions.str_to_float(response)
