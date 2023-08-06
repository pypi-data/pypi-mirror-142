from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:LINK \n
		Snippet: driver.applications.k9X11Ad.calculate.marker.link.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines whether all markers within the selected result display are linked. If enabled, and you move one
		marker along the x-axis, all other markers in the display are moved to the same x-axis position. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:LINK \n
		Snippet: value: bool = driver.applications.k9X11Ad.calculate.marker.link.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines whether all markers within the selected result display are linked. If enabled, and you move one
		marker along the x-axis, all other markers in the display are moved to the same x-axis position. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK?')
		return Conversions.str_to_bool(response)
