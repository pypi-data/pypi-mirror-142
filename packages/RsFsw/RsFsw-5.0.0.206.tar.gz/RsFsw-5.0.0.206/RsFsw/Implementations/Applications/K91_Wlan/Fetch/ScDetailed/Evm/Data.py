from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:SCDetailed:EVM:DATA \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.scDetailed.evm.data.get() \n
		Returns the EVM for all data subcarriers. The result is a comma-separated list of values, one for each PPDU and each RU.
		These results are only available if the Signal Content Detailed result display is currently active (see method RsFsw.
		Layout.Add.Window.get_) . \n
			:return: result: Unit: dB"""
		response = self._core.io.query_str(f'FETCh:SCDetailed:EVM:DATA?')
		return trim_str_response(response)
