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

	def get(self, query_range: enums.SelectionRangeB) -> int:
		"""SCPI: [SENSe]:PULSe:NUMBer \n
		Snippet: value: int = driver.applications.k6Pulse.sense.pulse.number.get(query_range = enums.SelectionRangeB.ALL) \n
		Queries the detected pulse numbers, i.e. the index within the capture buffer (as opposed to [SENSe:]PULSe:ID?) . \n
			:param query_range: CURRent | ALL CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: pulse_number: No help available"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:PULSe:NUMBer? {param}')
		return Conversions.str_to_int(response)
