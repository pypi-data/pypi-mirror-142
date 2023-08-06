from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, yaxis: enums.PulseTimingItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:TIMing:Y \n
		Snippet: driver.applications.k6Pulse.calculate.trend.timing.y.set(yaxis = enums.PulseTimingItems.DCYCle, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display.
		The x-axis is configured using the CALCulate<n>:TRENd:<GroupName>:X commands. \n
			:param yaxis: TSTamp | SETTling | RISE | FALL | PWIDth | OFF | DRATio | DCYCle | PRI | PRF Pulse parameter to be displayed on the y-axis. For a description of the available parameters see 'Timing parameters'. TSTamp Timestamp SETTling Settling Time RISE Rise Time FALL Fall Time PWIDth Pulse Width (ON Time) OFF Off Time DRATio Duty Ratio DCYCle Duty Cycle (%) PRI Pulse Repetition Interval PRF Pulse Repetition Frequency (Hz)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.PulseTimingItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:TIMing:Y {param}')
