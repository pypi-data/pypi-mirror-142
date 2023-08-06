from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pexcursion:
	"""Pexcursion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pexcursion", core, parent)

	def set(self, excursion: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer:PEXCursion \n
		Snippet: driver.applications.k60Transient.calculate.marker.pexcursion.set(excursion = 1.0, window = repcap.Window.Default) \n
		This command defines the peak excursion (for all markers in all windows) . The peak excursion sets the requirements for a
		peak to be detected during a peak search. The unit depends on the measurement. \n
			:param excursion: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(excursion)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer:PEXCursion {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer:PEXCursion \n
		Snippet: value: float = driver.applications.k60Transient.calculate.marker.pexcursion.get(window = repcap.Window.Default) \n
		This command defines the peak excursion (for all markers in all windows) . The peak excursion sets the requirements for a
		peak to be detected during a peak search. The unit depends on the measurement. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: excursion: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer:PEXCursion?')
		return Conversions.str_to_float(response)
