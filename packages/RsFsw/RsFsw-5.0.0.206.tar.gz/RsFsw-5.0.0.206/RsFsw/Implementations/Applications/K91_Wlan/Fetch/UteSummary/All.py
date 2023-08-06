from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:UTESummary:ALL \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.uteSummary.all.get() \n
		Returns the results of the Unused Tone Error Summary. The result is a comma-separated list of values for up to 37
		measurement points in the channel. Which subcarriers are measured depends on the size and position of the RU being
		transmitted. This result is required by the IEEE 802.11ax standard for HE trigger-based PPDUs with a maximum channel
		bandwidth of 80 MHz. \n
			:return: result: -35 dB LHS | RUIdx-3 | RUIdx-2 | RUIdx-1 | RUIdx | RUIdx+1 | RUIdx+2 | RUIdx+3 | -35 dB RHS Set of n subcarriers, where n is the number of subcarriers in the resource unit to be checked. For details see 'Unused tone error' Unit: -"""
		response = self._core.io.query_str(f'FETCh:UTESummary:ALL?')
		return trim_str_response(response)
