from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Feed:
	"""Feed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("feed", core, parent)

	def set(self, evaluation: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: driver.calculate.feed.set(evaluation = '1', window = repcap.Window.Default) \n
		This command selects the evaluation method of the measured data that is to be displayed in the specified window.
		Note that this command is maintained for compatibility reasons only. Use the LAYout commands for new remote control
		programs (see 'Working with windows in the display') . \n
			:param evaluation: Type of evaluation you want to display. See the table below for available parameter values.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(evaluation)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FEED {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: value: str = driver.calculate.feed.get(window = repcap.Window.Default) \n
		This command selects the evaluation method of the measured data that is to be displayed in the specified window.
		Note that this command is maintained for compatibility reasons only. Use the LAYout commands for new remote control
		programs (see 'Working with windows in the display') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: evaluation: Type of evaluation you want to display. See the table below for available parameter values."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FEED?')
		return trim_str_response(response)
