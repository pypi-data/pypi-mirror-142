from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:COUNt:FREQuency \n
		Snippet: value: float = driver.calculate.marker.count.frequency.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the frequency at the marker position. To get a valid result, you have to perform a complete
		measurement with synchronization to the end of the measurement before reading out the result. This is only possible for
		single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. Before you can use the command,
		you have to turn on the frequency counter. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: frequency: Frequency at the marker position."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:COUNt:FREQuency?')
		return Conversions.str_to_float(response)
