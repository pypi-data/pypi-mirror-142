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

	def set(self, xaxis: enums.PulsePowerItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:POWer:X \n
		Snippet: driver.applications.k6Pulse.calculate.trend.power.x.set(xaxis = enums.PulsePowerItems.ADDB, window = repcap.Window.Default) \n
		Configures the x-axis of the Parameter Trend result display.
		The y-axis is configured using the CALCulate<n>:TRENd:<GroupName>:Y commands. \n
			:param xaxis: TOP | BASE | AMPLitude | ON | AVG | MIN | MAX | PON | PAVG | PMIN | ADPercent | ADDB | RPERcent | RDB | OPERcent | ODB | POINt | PPRatio | I | Q Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Power/amplitude parameters'. TOP Top Power BASE Base Power AMPLitude Pulse Amplitude ON Average ON Power AVG Average Tx Power MIN Minimum Power MAX Peak Power PON Peak-to-Avg ON Power Ratio PAVG Peak-to-Average Tx Power Ratio PMIN Peak-to-Min Power Ratio ADPercent Droop in % ADDB Droop in dB RPERcent Ripple in % RDB Ripple in dB OPERcent Overshoot in % ODB Overshoot in dB POINt Pulse power measured at measurement point PPRatio Pulse-to-Pulse Power Difference
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(xaxis, enums.PulsePowerItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:POWer:X {param}')
