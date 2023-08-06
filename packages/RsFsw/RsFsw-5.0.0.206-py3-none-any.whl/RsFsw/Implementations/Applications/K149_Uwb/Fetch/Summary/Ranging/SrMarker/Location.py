from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Location:
	"""Location commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("location", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: FETCh<n>:SUMMary:RANGing:SRMarker<m>:LOCation \n
		Snippet: value: float = driver.applications.k149Uwb.fetch.summary.ranging.srMarker.location.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SrMarker')
			:return: result: numeric value"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:SUMMary:RANGing:SRMarker{marker_cmd_val}:LOCation?')
		return Conversions.str_to_float(response)
