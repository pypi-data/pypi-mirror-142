from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:NDBDown:RESult \n
		Snippet: value: float = driver.calculate.marker.function.ndbDown.result.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the distance of the n dB down markers from each other. To get a valid result, you have to perform a
		complete measurement with synchronization to the end of the measurement before reading out the result. This is only
		possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: distance: The result depends on the span. In case of frequency domain measurements, the command returns the bandwidth between the two n dB down markers in Hz. In case of time domain measurements, the command returns the pulse width between the two n dB down markers in seconds."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:NDBDown:RESult?')
		return Conversions.str_to_float(response)
