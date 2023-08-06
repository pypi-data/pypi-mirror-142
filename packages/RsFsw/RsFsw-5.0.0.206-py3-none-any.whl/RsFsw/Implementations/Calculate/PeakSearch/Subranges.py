from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subranges:
	"""Subranges commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subranges", core, parent)

	def set(self, number_peaks: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSEarch:SUBRanges \n
		Snippet: driver.calculate.peakSearch.subranges.set(number_peaks = 1.0, window = repcap.Window.Default) \n
		This command defines the number of peaks included in the peak list. After this number of peaks has been found, the R&S
		FSW stops the peak search and continues the search in the next measurement range. \n
			:param number_peaks: Range: 1 to 50
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(number_peaks)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSEarch:SUBRanges {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PSEarch:SUBRanges \n
		Snippet: value: float = driver.calculate.peakSearch.subranges.get(window = repcap.Window.Default) \n
		This command defines the number of peaks included in the peak list. After this number of peaks has been found, the R&S
		FSW stops the peak search and continues the search in the next measurement range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: number_peaks: Range: 1 to 50"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSEarch:SUBRanges?')
		return Conversions.str_to_float(response)
