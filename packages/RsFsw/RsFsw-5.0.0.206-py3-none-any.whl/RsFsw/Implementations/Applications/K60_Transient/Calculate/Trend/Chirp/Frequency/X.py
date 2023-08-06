from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, xaxis: enums.AxisFreqItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:CHIRp:FREQuency:X \n
		Snippet: driver.applications.k60Transient.calculate.trend.chirp.frequency.x.set(xaxis = enums.AxisFreqItems.AVGFm, window = repcap.Window.Default) \n
		Configures the x-axis of the Parameter Trend result display for chirp frequency parameters. \n
			:param xaxis: AVGFm | AVGNonlinear | BWIDth | CHERror | FREQuency | MAXFm | MAXNonlinear | RMSFm | RMSNonlinear CHERror Chirp state deviation FREQuency Average frequency MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length BWIDth Bandwidth AVGNonlinear Average frequency non-linearity RMSNonlinear RMS frequency non-linearity MAXNonlinear Peak frequency non-linearity PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(xaxis, enums.AxisFreqItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:CHIRp:FREQuency:X {param}')
