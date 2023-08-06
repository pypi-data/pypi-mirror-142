from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcmGain:
	"""PcmGain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcmGain", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:PCMGain \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.pcmGain.get() \n
		This command returns the physical channel gain result which is used as the reference for the Spectrum Flatness limits
		when Spectrum Flatness results are based on physical channels (see method RsFsw.Applications.K91_Wlan.Configure.Burst.
		Spectrum.Flatness.Cselect.set) . For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:return: result: comma-separated list of values; one value for each RX stream Unit: dBm"""
		response = self._core.io.query_str(f'FETCh:BURSt:PCMGain?')
		return trim_str_response(response)
