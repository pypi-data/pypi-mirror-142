from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchSignal:
	"""SearchSignal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("searchSignal", core, parent)

	def set(self, event: enums.EventOnce, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:MDEPth:SEARchsignal \n
		Snippet: driver.calculate.marker.function.mdepth.searchSignal.set(event = enums.EventOnce.ONCE, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command initiates a search for the signals required for the AM depth measurement. Note that the command does not
		perform a new measurement, but looks for the signals on the current trace. \n
			:param event: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(event, enums.EventOnce)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:MDEPth:SEARchsignal {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.EventOnce:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:MDEPth:SEARchsignal \n
		Snippet: value: enums.EventOnce = driver.calculate.marker.function.mdepth.searchSignal.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command initiates a search for the signals required for the AM depth measurement. Note that the command does not
		perform a new measurement, but looks for the signals on the current trace. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: event: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:MDEPth:SEARchsignal?')
		return Conversions.str_to_scalar_enum(response, enums.EventOnce)
