from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def get(self, query_range: enums.SelectionRange) -> str:
		"""SCPI: [SENSe]:PULSe:POWer:AMPLitude:LIMit \n
		Snippet: value: str = driver.applications.k6Pulse.sense.pulse.power.amplitude.limit.get(query_range = enums.SelectionRange.ALL) \n
		Returns a comma-separated list of results for the limit check for the specified parameter and number of pulses.
		For details on available parameters see 'Pulse parameters'. The limit check for an individual parameter is defined using
		the CALCulate<n>:TABLe:<ParameterGroup>:<Parameter>:LIMit:STATe commands. Commands for the parameter group <TSIDelobe>
		are only available if the additional option R&S FSW-K6S is installed. \n
			:param query_range: SELected | CURRent | ALL Determines which pulses are checked against the limits SELected Currently selected pulse CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: check_result: char_data"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRange)
		response = self._core.io.query_str(f'SENSe:PULSe:POWer:AMPLitude:LIMit? {param}')
		return trim_str_response(response)
