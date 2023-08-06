from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaxFrequency:
	"""MaxFrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maxFrequency", core, parent)

	def set(self, max_frequncy: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSPectrum:MAXFrequency \n
		Snippet: driver.applications.k6Pulse.calculate.pspectrum.maxFrequency.set(max_frequncy = 1.0, window = repcap.Window.Default) \n
		Defines the maximum frequency span for which the Pulse-to-Pulse Spectrum is calculated. Internally, the span is limited
		by the number of possible interpolation samples (100 000) . \n
			:param max_frequncy: Range: 0 to 1/10 of sample rate, Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(max_frequncy)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSPectrum:MAXFrequency {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PSPectrum:MAXFrequency \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.pspectrum.maxFrequency.get(window = repcap.Window.Default) \n
		Defines the maximum frequency span for which the Pulse-to-Pulse Spectrum is calculated. Internally, the span is limited
		by the number of possible interpolation samples (100 000) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: max_frequncy: Range: 0 to 1/10 of sample rate, Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:MAXFrequency?')
		return Conversions.str_to_float(response)
