from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> int:
		"""SCPI: [SENSe]:PULSe:COUNt \n
		Snippet: value: int = driver.applications.k6Pulse.sense.pulse.count.get(query_range = enums.SelectionRangeB.ALL) \n
		Queries the number of detected pulses in the current capture buffer or the entire measurement. \n
			:param query_range: CURRent | ALL CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:PULSe:COUNt? {param}')
		return Conversions.str_to_int(response)
