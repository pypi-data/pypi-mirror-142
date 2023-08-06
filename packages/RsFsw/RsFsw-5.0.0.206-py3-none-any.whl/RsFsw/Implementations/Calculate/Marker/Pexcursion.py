from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pexcursion:
	"""Pexcursion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pexcursion", core, parent)

	def set(self, excursion: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:PEXCursion \n
		Snippet: driver.calculate.marker.pexcursion.set(excursion = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the peak excursion (for all markers in all windows) . The peak excursion sets the requirements for a
		peak to be detected during a peak search. The unit depends on the measurement.
			Table Header: Application/Result display / Unit \n
			- Spectrum / dB
			- ADEMOD, RF / dB
			- ADEMOD, AM / PCT
			- ADEMOD, FM / kHz
			- ADEMOD, PM / RAD \n
			:param excursion: The excursion is the distance to a trace maximum that must be attained before a new maximum is recognized, or the distance to a trace minimum that must be attained before a new minimum is recognized
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(excursion)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:PEXCursion {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:PEXCursion \n
		Snippet: value: float = driver.calculate.marker.pexcursion.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the peak excursion (for all markers in all windows) . The peak excursion sets the requirements for a
		peak to be detected during a peak search. The unit depends on the measurement.
			Table Header: Application/Result display / Unit \n
			- Spectrum / dB
			- ADEMOD, RF / dB
			- ADEMOD, AM / PCT
			- ADEMOD, FM / kHz
			- ADEMOD, PM / RAD \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: excursion: The excursion is the distance to a trace maximum that must be attained before a new maximum is recognized, or the distance to a trace minimum that must be attained before a new minimum is recognized"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:PEXCursion?')
		return Conversions.str_to_float(response)
