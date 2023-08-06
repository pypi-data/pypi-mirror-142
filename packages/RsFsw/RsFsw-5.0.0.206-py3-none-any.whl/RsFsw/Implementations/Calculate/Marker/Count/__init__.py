from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def resolution(self):
		"""resolution commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resolution'):
			from .Resolution import Resolution
			self._resolution = Resolution(self._core, self._cmd_group)
		return self._resolution

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	def set(self, state: bool, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:COUNt \n
		Snippet: driver.calculate.marker.count.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command turns the frequency counter at the marker position on and off. The frequency counter works for one marker
		only. If you perform a frequency count with another marker, the R&S FSW deactivates the frequency count of the first
		marker. To get a valid result, you have to perform a complete measurement with synchronization to the end of the
		measurement before reading out the result. This is only possible for single sweep mode. See also method RsFsw.
		Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:COUNt {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:COUNt \n
		Snippet: value: bool = driver.calculate.marker.count.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command turns the frequency counter at the marker position on and off. The frequency counter works for one marker
		only. If you perform a frequency count with another marker, the R&S FSW deactivates the frequency count of the first
		marker. To get a valid result, you have to perform a complete measurement with synchronization to the end of the
		measurement before reading out the result. This is only possible for single sweep mode. See also method RsFsw.
		Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:COUNt?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
