from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Feed:
	"""Feed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("feed", core, parent)

	def set(self, feed: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: driver.applications.k70Vsa.calculate.feed.set(feed = '1', window = repcap.Window.Default) \n
		Selects the signal source (and for the equalizer also the result type) for evaluation. Selects the signal source (and for
		the equalizer and multi-source diagrams also the result type) for evaluation. Note that this command is maintained for
		compatibility reasons only. Use the LAYout commands for new remote control programs (see 'Working with windows in the
		display') . Only for the 'Equalizer Impulse Response' and 'Equalizer Frequency Response', as well as the multi-source
		diagrams, this command is required. \n
			:param feed: string 'XTIM:DDEM:MEAS' Measured signal 'XTIM:DDEM:REF' Reference signal 'XTIM:DDEM:ERR:VECT' Error vector 'XTIM:DDEM:ERR:MPH' Modulation errors 'XTIM:DDEM:MACC' Modulation accuracy 'XTIM:DDEM:SYMB' Symbol table 'TCAP' Capture Buffer 'XTIM:DDEM:IMP' Equalizer Impulse Response 'XFR:DDEM:RAT' Equalizer Frequency Response 'XFR:DDEM:IRAT' Equalizer Channel Frequency Response Group Delay XTIM:DDEM:TCAP:ERR Spectrum of Real/Imag for capture buffer and error vector XTIM:DDEM:MEAS:ERR Spectrum of Real/Imag for measurement and error vector
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(feed)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FEED {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: value: str = driver.applications.k70Vsa.calculate.feed.get(window = repcap.Window.Default) \n
		Selects the signal source (and for the equalizer also the result type) for evaluation. Selects the signal source (and for
		the equalizer and multi-source diagrams also the result type) for evaluation. Note that this command is maintained for
		compatibility reasons only. Use the LAYout commands for new remote control programs (see 'Working with windows in the
		display') . Only for the 'Equalizer Impulse Response' and 'Equalizer Frequency Response', as well as the multi-source
		diagrams, this command is required. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: feed: string 'XTIM:DDEM:MEAS' Measured signal 'XTIM:DDEM:REF' Reference signal 'XTIM:DDEM:ERR:VECT' Error vector 'XTIM:DDEM:ERR:MPH' Modulation errors 'XTIM:DDEM:MACC' Modulation accuracy 'XTIM:DDEM:SYMB' Symbol table 'TCAP' Capture Buffer 'XTIM:DDEM:IMP' Equalizer Impulse Response 'XFR:DDEM:RAT' Equalizer Frequency Response 'XFR:DDEM:IRAT' Equalizer Channel Frequency Response Group Delay XTIM:DDEM:TCAP:ERR Spectrum of Real/Imag for capture buffer and error vector XTIM:DDEM:MEAS:ERR Spectrum of Real/Imag for measurement and error vector"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FEED?')
		return trim_str_response(response)
