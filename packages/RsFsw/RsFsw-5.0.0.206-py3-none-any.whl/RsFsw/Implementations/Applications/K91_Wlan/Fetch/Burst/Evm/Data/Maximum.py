from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:EVM:DATA:MAXimum \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.evm.data.maximum.get() \n
		This command returns the average, maximum or minimum EVM for the data carrier in dB. For details see 'Modulation accuracy,
		flatness and tolerance parameters'. \n
			:return: result: Global Result, Stream 1 result ... Stream n result"""
		response = self._core.io.query_str(f'FETCh:BURSt:EVM:DATA:MAXimum?')
		return trim_str_response(response)
