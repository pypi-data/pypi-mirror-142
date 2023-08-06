from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Left:
	"""Left commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("left", core, parent)

	def set(self, left_limit: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:X:SLIMits:LEFT \n
		Snippet: driver.applications.k70Vsa.calculate.marker.x.slimits.left.set(left_limit = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the left limit of the marker search range for all markers in all windows.
		If you perform a measurement in the time domain, this command limits the range of the trace to be analyzed. \n
			:param left_limit: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(left_limit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X:SLIMits:LEFT {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:X:SLIMits:LEFT \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.marker.x.slimits.left.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the left limit of the marker search range for all markers in all windows.
		If you perform a measurement in the time domain, this command limits the range of the trace to be analyzed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: left_limit: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:X:SLIMits:LEFT?')
		return Conversions.str_to_float(response)
