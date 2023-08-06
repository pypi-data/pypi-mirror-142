from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, xaxis: enums.PulseFreqItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:FREQuency:X \n
		Snippet: driver.applications.k6Pulse.calculate.trend.frequency.x.set(xaxis = enums.PulseFreqItems.CRATe, window = repcap.Window.Default) \n
		Configures the x-axis of the Parameter Trend result display.
		The y-axis is configured using the CALCulate<n>:TRENd:<GroupName>:Y commands. \n
			:param xaxis: POINt | PPFRequency | RERRor | PERRor | DEViation | CRATe Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Frequency parameters'. POINt Frequency at measurement point PPFRequency Pulse-Pulse Frequency Difference RERRor Frequency Error (RMS) PERRor Frequency Error (Peak) DEViation Frequency Deviation CRATe Chirp Rate
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(xaxis, enums.PulseFreqItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:FREQuency:X {param}')
