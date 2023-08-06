from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sort:
	"""Sort commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sort", core, parent)

	def set(self, sort_mode: enums.FpeaksSortMode, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:FPEaks:SORT \n
		Snippet: driver.calculate.marker.function.fpeaks.sort.set(sort_mode = enums.FpeaksSortMode.X, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command selects the order in which the results of a peak search are returned. \n
			:param sort_mode: X Sorts the peaks according to increasing position on the x-axis. Y Sorts the peaks according to decreasing position on the y-axis.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(sort_mode, enums.FpeaksSortMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:FPEaks:SORT {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.FpeaksSortMode:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:FPEaks:SORT \n
		Snippet: value: enums.FpeaksSortMode = driver.calculate.marker.function.fpeaks.sort.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command selects the order in which the results of a peak search are returned. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: sort_mode: X Sorts the peaks according to increasing position on the x-axis. Y Sorts the peaks according to decreasing position on the y-axis."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:FPEaks:SORT?')
		return Conversions.str_to_scalar_enum(response, enums.FpeaksSortMode)
