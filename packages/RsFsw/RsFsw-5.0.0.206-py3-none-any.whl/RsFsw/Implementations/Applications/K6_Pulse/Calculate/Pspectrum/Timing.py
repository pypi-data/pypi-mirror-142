from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timing:
	"""Timing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	def set(self, param: enums.PulseTimingItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSPectrum:TIMing \n
		Snippet: driver.applications.k6Pulse.calculate.pspectrum.timing.set(param = enums.PulseTimingItems.DCYCle, window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param param: TSTamp | SETTling | RISE | FALL | PWIDth | OFF | DRATio | DCYCle | PRI | PRF Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Timing parameters'. TSTamp Timestamp SETTling Settling Time RISE Rise Time FALL Fall Time PWIDth Pulse Width (ON Time) OFF Off Time DRATio Duty Ratio DCYCle Duty Cycle (%) PRI Pulse Repetition Interval PRF Pulse Repetition Frequency (Hz)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(param, enums.PulseTimingItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSPectrum:TIMing {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PulseTimingItems:
		"""SCPI: CALCulate<n>:PSPectrum:TIMing \n
		Snippet: value: enums.PulseTimingItems = driver.applications.k6Pulse.calculate.pspectrum.timing.get(window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: param: TSTamp | SETTling | RISE | FALL | PWIDth | OFF | DRATio | DCYCle | PRI | PRF Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Timing parameters'. TSTamp Timestamp SETTling Settling Time RISE Rise Time FALL Fall Time PWIDth Pulse Width (ON Time) OFF Off Time DRATio Duty Ratio DCYCle Duty Cycle (%) PRI Pulse Repetition Interval PRF Pulse Repetition Frequency (Hz)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:TIMing?')
		return Conversions.str_to_scalar_enum(response, enums.PulseTimingItems)
