from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Margin:
	"""Margin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("margin", core, parent)

	def set(self, margin: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:ESPectrum:PSEarch:MARGin \n
		Snippet: driver.applications.k149Uwb.calculate.espectrum.peakSearch.margin.set(margin = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param margin: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(margin)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:ESPectrum:PSEarch:MARGin {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:ESPectrum:PSEarch:MARGin \n
		Snippet: value: float = driver.applications.k149Uwb.calculate.espectrum.peakSearch.margin.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: margin: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:ESPectrum:PSEarch:MARGin?')
		return Conversions.str_to_float(response)
