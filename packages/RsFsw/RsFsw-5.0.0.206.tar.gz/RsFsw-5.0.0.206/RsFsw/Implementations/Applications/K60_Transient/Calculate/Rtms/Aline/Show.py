from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Show:
	"""Show commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("show", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RTMS:ALINe:SHOW \n
		Snippet: driver.applications.k60Transient.calculate.rtms.aline.show.set(state = False, window = repcap.Window.Default) \n
		This command defines whether or not the analysis line is displayed in all time-based windows in all MSRT secondary
		applications and the MSRT primary. Note: even if the analysis line display is off, the indication whether or not the
		currently defined line position lies within the analysis interval of the active secondary application remains in the
		window title bars. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RTMS:ALINe:SHOW {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:RTMS:ALINe:SHOW \n
		Snippet: value: bool = driver.applications.k60Transient.calculate.rtms.aline.show.get(window = repcap.Window.Default) \n
		This command defines whether or not the analysis line is displayed in all time-based windows in all MSRT secondary
		applications and the MSRT primary. Note: even if the analysis line display is off, the indication whether or not the
		currently defined line position lies within the analysis interval of the active secondary application remains in the
		window title bars. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RTMS:ALINe:SHOW?')
		return Conversions.str_to_bool(response)
