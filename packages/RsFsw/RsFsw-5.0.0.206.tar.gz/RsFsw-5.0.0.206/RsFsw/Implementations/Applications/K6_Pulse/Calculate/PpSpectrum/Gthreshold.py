from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gthreshold:
	"""Gthreshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gthreshold", core, parent)

	def set(self, gap_threshold: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PPSPectrum:GTHReshold \n
		Snippet: driver.applications.k6Pulse.calculate.ppSpectrum.gthreshold.set(gap_threshold = 1.0, window = repcap.Window.Default) \n
		Defines the minimum time that must pass before a gap is detected as such. For more information see 'Parameter spectrum
		calculation'. \n
			:param gap_threshold: Range: minimum spacing between pulses to meas time, Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(gap_threshold)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PPSPectrum:GTHReshold {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PPSPectrum:GTHReshold \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.ppSpectrum.gthreshold.get(window = repcap.Window.Default) \n
		Defines the minimum time that must pass before a gap is detected as such. For more information see 'Parameter spectrum
		calculation'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: gap_threshold: Range: minimum spacing between pulses to meas time, Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PPSPectrum:GTHReshold?')
		return Conversions.str_to_float(response)
