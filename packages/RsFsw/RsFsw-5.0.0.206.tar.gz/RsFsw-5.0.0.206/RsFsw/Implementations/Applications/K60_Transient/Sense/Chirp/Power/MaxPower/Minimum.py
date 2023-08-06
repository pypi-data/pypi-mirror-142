from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> float:
		"""SCPI: [SENSe]:CHIRp:POWer:MAXPower:MINimum \n
		Snippet: value: float = driver.applications.k60Transient.sense.chirp.power.maxPower.minimum.get(query_range = enums.SelectionRangeB.ALL) \n
		Returns the statistical value for the Chirp Maximum Power from the statistics table for the specified chirp(s) . \n
			:param query_range: CURRent | ALL CURRent Detected chirps in the current capture buffer ALL All chirps detected in the entire measurement
			:return: result: CURRent | ALL CURRent Detected chirps in the current capture buffer ALL All chirps detected in the entire measurement"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:CHIRp:POWer:MAXPower:MINimum? {param}')
		return Conversions.str_to_float(response)
