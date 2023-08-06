from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EcmGain:
	"""EcmGain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ecmGain", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:ECMGain \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.ecmGain.get() \n
		This command returns the effective channel gain result which is used as the reference for the Spectrum Flatness limits
		when Spectrum Flatness results are based on effective channels (see method RsFsw.Applications.K91_Wlan.Configure.Burst.
		Spectrum.Flatness.Cselect.set) . For details see 'Modulation accuracy, flatness and tolerance parameters'. \n
			:return: result: comma-separated list of values; one value for each RX stream Unit: dBm"""
		response = self._core.io.query_str(f'FETCh:BURSt:ECMGain?')
		return trim_str_response(response)
