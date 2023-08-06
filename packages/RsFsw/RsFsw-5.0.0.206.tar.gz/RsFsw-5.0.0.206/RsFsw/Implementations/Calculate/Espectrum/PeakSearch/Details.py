from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Details:
	"""Details commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("details", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:ESPectrum:PSEarch:DETails \n
		Snippet: driver.calculate.espectrum.peakSearch.details.set(state = False, window = repcap.Window.Default) \n
		This command configures how detailed the list in the Result Summary is. \n
			:param state: ON | OFF | 1 | 0 ON | 1 Includes all detected peaks (up to a maximum defined by CALCulaten:PEAKsearch:SUBRanges) . OFF | 0 Includes only one peak per range.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:ESPectrum:PSEarch:DETails {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:ESPectrum:PSEarch:DETails \n
		Snippet: value: bool = driver.calculate.espectrum.peakSearch.details.get(window = repcap.Window.Default) \n
		This command configures how detailed the list in the Result Summary is. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0 ON | 1 Includes all detected peaks (up to a maximum defined by CALCulaten:PEAKsearch:SUBRanges) . OFF | 0 Includes only one peak per range."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:ESPectrum:PSEarch:DETails?')
		return Conversions.str_to_bool(response)
