from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, param: enums.PulsePowerItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSPectrum:POWer \n
		Snippet: driver.applications.k6Pulse.calculate.pspectrum.power.set(param = enums.PulsePowerItems.ADDB, window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param param: TOP | BASE | AMPLitude | ON | AVG | MIN | MAX | PON | PAVG | PMIN | ADPercent | ADDB | RPERcent | RDB | OPERcent | ODB | POINt | PPRatio | I | Q Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Phase parameters'. TOP Top Power BASE Base Power AMPLitude Pulse Amplitude ON Average ON Power AVG Average Tx Power MIN Minimum Power MAX Peak Power PON Peak-to-Avg ON Power Ratio PAVG Peak-to-Average Tx Power Ratio PMIN Peak-to-Min Power Ratio ADPercent Droop in % ADDB Droop in dB RPERcent Ripple in % RDB Ripple in dB OPERcent Overshoot in % ODB Overshoot in dB POINt Pulse power measured at measurement point PPRatio Pulse-to-Pulse Power Difference
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(param, enums.PulsePowerItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSPectrum:POWer {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PulsePowerItems:
		"""SCPI: CALCulate<n>:PSPectrum:POWer \n
		Snippet: value: enums.PulsePowerItems = driver.applications.k6Pulse.calculate.pspectrum.power.get(window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: param: TOP | BASE | AMPLitude | ON | AVG | MIN | MAX | PON | PAVG | PMIN | ADPercent | ADDB | RPERcent | RDB | OPERcent | ODB | POINt | PPRatio | I | Q Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Phase parameters'. TOP Top Power BASE Base Power AMPLitude Pulse Amplitude ON Average ON Power AVG Average Tx Power MIN Minimum Power MAX Peak Power PON Peak-to-Avg ON Power Ratio PAVG Peak-to-Average Tx Power Ratio PMIN Peak-to-Min Power Ratio ADPercent Droop in % ADDB Droop in dB RPERcent Ripple in % RDB Ripple in dB OPERcent Overshoot in % ODB Overshoot in dB POINt Pulse power measured at measurement point PPRatio Pulse-to-Pulse Power Difference"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.PulsePowerItems)
