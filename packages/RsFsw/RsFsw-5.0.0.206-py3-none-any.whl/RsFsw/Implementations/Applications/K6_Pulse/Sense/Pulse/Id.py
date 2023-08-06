from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> int:
		"""SCPI: [SENSe]:PULSe:ID \n
		Snippet: value: int = driver.applications.k6Pulse.sense.pulse.id.get(query_range = enums.SelectionRangeB.ALL) \n
		Queries the ids of the detected pulses, i.e the unique index within the entire measurement (as opposed to
		[SENSe:]PULSe:NUMBer?) . \n
			:param query_range: CURRent | ALL CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: pulse_id: No help available"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:PULSe:ID? {param}')
		return Conversions.str_to_int(response)
