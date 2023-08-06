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
		Snippet: driver.applications.k70Vsa.calculate.marker.link.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		With this command markers between several screens can be coupled, i.e. use the same x-value. All screens can be linked
		with the marker x-value scaled in symbols or time, except those showing the capture buffer. If several capture buffer
		measurements are visible, their markers are coupled, too. \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:LINK \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.marker.link.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		With this command markers between several screens can be coupled, i.e. use the same x-value. All screens can be linked
		with the marker x-value scaled in symbols or time, except those showing the capture buffer. If several capture buffer
		measurements are visible, their markers are coupled, too. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:LINK?')
		return Conversions.str_to_bool(response)
