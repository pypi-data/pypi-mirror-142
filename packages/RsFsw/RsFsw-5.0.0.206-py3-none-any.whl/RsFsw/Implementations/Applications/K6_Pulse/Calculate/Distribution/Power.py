from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, xaxis: enums.PulsePowerItems, yaxis: enums.YaXisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DISTribution:POWer \n
		Snippet: driver.applications.k6Pulse.calculate.distribution.power.set(xaxis = enums.PulsePowerItems.ADDB, yaxis = enums.YaXisItems.COUNt, window = repcap.Window.Default) \n
		Configures the Parameter Distribution result display. \n
			:param xaxis: TOP | BASE | AMPLitude | ON | AVG | MIN | MAX | PON | PAVG | PMIN | ADPercent | ADDB | RPERcent | RDB | OPERcent | ODB | POINt | PPRatio | I | Q Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Phase parameters'. TOP Top Power BASE Base Power AMPLitude Pulse Amplitude ON Average ON Power AVG Average Tx Power MIN Minimum Power MAX Peak Power PON Peak-to-Avg ON Power Ratio PAVG Peak-to-Average Tx Power Ratio PMIN Peak-to-Min Power Ratio ADPercent Droop in % ADDB Droop in dB RPERcent Ripple in % RDB Ripple in dB OPERcent Overshoot in % ODB Overshoot in dB POINt Pulse power measured at measurement point PPRatio Pulse-to-Pulse Power Difference
			:param yaxis: COUNt | OCCurrence Parameter to be displayed on the y-axis. COUNt Number of pulses in which the parameter value occurred. OCCurrence Percentage of all measured pulses in which the parameter value occurred.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulsePowerItems), ArgSingle('yaxis', yaxis, DataType.Enum, enums.YaXisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DISTribution:POWer {param}'.rstrip())
