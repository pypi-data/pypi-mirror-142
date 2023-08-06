from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:PREamble:MINimum \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.preamble.minimum.get() \n
		This command returns the average, maximum or minimum of the 'Preamble Power per PPDU' (in dBm) . All symbols prior to the
		first data symbol of the PPDU are used to calculate the preamble power. All analyzed PPDUs, up to the statistic length,
		take part in the statistical evaluation. \n
			:return: result: list"""
		response = self._core.io.query_str(f'FETCh:BURSt:PREamble:MINimum?')
		return trim_str_response(response)
