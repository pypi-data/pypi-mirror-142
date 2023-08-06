from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Resolution:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, resolution: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:COUNt:RESolution \n
		Snippet: driver.calculate.marker.count.resolution.set(resolution = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the resolution of the frequency counter. \n
			:param resolution: 0.001 | 0.01 | 0.1 | 1 | 10 | 100 | 1000 | 10000 Hz Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(resolution)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:COUNt:RESolution {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:COUNt:RESolution \n
		Snippet: value: float = driver.calculate.marker.count.resolution.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the resolution of the frequency counter. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: resolution: 0.001 | 0.01 | 0.1 | 1 | 10 | 100 | 1000 | 10000 Hz Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:COUNt:RESolution?')
		return Conversions.str_to_float(response)
