from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, timeLine=repcap.TimeLine.Default) -> None:
		"""SCPI: CALCulate<n>:TLINe<dl>:STATe \n
		Snippet: driver.calculate.tline.state.set(state = False, window = repcap.Window.Default, timeLine = repcap.TimeLine.Default) \n
		This command turns a time line on and off \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param timeLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tline')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		timeLine_cmd_val = self._cmd_group.get_repcap_cmd_value(timeLine, repcap.TimeLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:TLINe{timeLine_cmd_val}:STATe {param}')

	def get(self, window=repcap.Window.Default, timeLine=repcap.TimeLine.Default) -> bool:
		"""SCPI: CALCulate<n>:TLINe<dl>:STATe \n
		Snippet: value: bool = driver.calculate.tline.state.get(window = repcap.Window.Default, timeLine = repcap.TimeLine.Default) \n
		This command turns a time line on and off \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param timeLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tline')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		timeLine_cmd_val = self._cmd_group.get_repcap_cmd_value(timeLine, repcap.TimeLine)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TLINe{timeLine_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
