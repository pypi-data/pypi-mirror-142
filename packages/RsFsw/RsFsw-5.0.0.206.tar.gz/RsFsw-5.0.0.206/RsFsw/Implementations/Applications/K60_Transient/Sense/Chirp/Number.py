from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Number:
	"""Number commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("number", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> float:
		"""SCPI: [SENSe]:CHIRp:NUMBer \n
		Snippet: value: float = driver.applications.k60Transient.sense.chirp.number.get(query_range = enums.SelectionRangeB.ALL) \n
		Returns the chirp numbers from the Results table for the specified chirp(s) . \n
			:param query_range: CURRent | ALL CURRent Detected chirps in the current capture buffer ALL All chirps detected in the entire measurement
			:return: result: CURRent | ALL CURRent Detected chirps in the current capture buffer ALL All chirps detected in the entire measurement"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:CHIRp:NUMBer? {param}')
		return Conversions.str_to_float(response)
