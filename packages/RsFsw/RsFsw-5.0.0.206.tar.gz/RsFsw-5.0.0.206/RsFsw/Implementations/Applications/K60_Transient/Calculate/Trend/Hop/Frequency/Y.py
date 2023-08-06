from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, yaxis: enums.AxisFreqFmItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:HOP:FREQuency:Y \n
		Snippet: driver.applications.k60Transient.calculate.trend.hop.frequency.y.set(yaxis = enums.AxisFreqFmItems.AVGFm, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display for hop frequency parameters. \n
			:param yaxis: AVGFm | FMERror | FREQuency | MAXFm | RELFrequency | RMSFm FREQuency Average frequency RELFrequency Relative frequency (hop-to-hop) FMERror Hop state deviation MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.AxisFreqFmItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:HOP:FREQuency:Y {param}')
