from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, offset_frequency: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:SNOise<m>:X \n
		Snippet: driver.applications.k40PhaseNoise.calculate.snoise.x.set(offset_frequency = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the horizontal position of a custom spot noise marker. \n
			:param offset_frequency: The minimum offset is 1 Hz. The maximum offset depends on the hardware you are using. The default value varies for each of the five spot noise markers. For marker 1 it is 1 kHz, for marker 2 it is 10 kHz, for marker 3 it is 100 kHz, for marker 4 it is 1 MHz and for marker 5 it is 10 MHz Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Snoise')
		"""
		param = Conversions.decimal_value_to_str(offset_frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:SNOise{marker_cmd_val}:X {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:SNOise<m>:X \n
		Snippet: value: float = driver.applications.k40PhaseNoise.calculate.snoise.x.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the horizontal position of a custom spot noise marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Snoise')
			:return: offset_frequency: The minimum offset is 1 Hz. The maximum offset depends on the hardware you are using. The default value varies for each of the five spot noise markers. For marker 1 it is 1 kHz, for marker 2 it is 10 kHz, for marker 3 it is 100 kHz, for marker 4 it is 1 MHz and for marker 5 it is 10 MHz Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:SNOise{marker_cmd_val}:X?')
		return Conversions.str_to_float(response)
