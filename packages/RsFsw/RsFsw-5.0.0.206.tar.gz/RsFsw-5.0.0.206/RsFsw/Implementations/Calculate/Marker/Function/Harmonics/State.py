from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:HARMonics[:STATe] \n
		Snippet: driver.calculate.marker.function.harmonics.state.set(state = False, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command turns the harmonic distortion measurement on and off. Note the following:
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- If you perform the measurement in the frequency domain, the search range for the frequency of the first harmonic, whose power is determined, is defined by the last span.
			- If you perform the measurement in the time domain, the current center frequency is used as the frequency of the first harmonic. Thus, the frequency search is bypassed. The first harmonic frequency is set by a specific center frequency in zero span before the harmonic measurement is started. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:HARMonics:STATe {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> bool:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:HARMonics[:STATe] \n
		Snippet: value: bool = driver.calculate.marker.function.harmonics.state.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command turns the harmonic distortion measurement on and off. Note the following:
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- If you perform the measurement in the frequency domain, the search range for the frequency of the first harmonic, whose power is determined, is defined by the last span.
			- If you perform the measurement in the time domain, the current center frequency is used as the frequency of the first harmonic. Thus, the frequency search is bypassed. The first harmonic frequency is set by a specific center frequency in zero span before the harmonic measurement is started. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:HARMonics:STATe?')
		return Conversions.str_to_bool(response)
