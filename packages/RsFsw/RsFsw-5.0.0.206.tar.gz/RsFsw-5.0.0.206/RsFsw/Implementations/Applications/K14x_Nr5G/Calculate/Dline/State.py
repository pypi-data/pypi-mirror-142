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

	def set(self, state: bool, window=repcap.Window.Default, displayLine=repcap.DisplayLine.Default) -> None:
		"""SCPI: CALCulate<n>:DLINe<li>:STATe \n
		Snippet: driver.applications.k14Xnr5G.calculate.dline.state.set(state = False, window = repcap.Window.Default, displayLine = repcap.DisplayLine.Default) \n
		No command help available \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param displayLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dline')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		displayLine_cmd_val = self._cmd_group.get_repcap_cmd_value(displayLine, repcap.DisplayLine)
		self._core.io.write(f'CALCulate{window_cmd_val}:DLINe{displayLine_cmd_val}:STATe {param}')

	def get(self, window=repcap.Window.Default, displayLine=repcap.DisplayLine.Default) -> bool:
		"""SCPI: CALCulate<n>:DLINe<li>:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.calculate.dline.state.get(window = repcap.Window.Default, displayLine = repcap.DisplayLine.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param displayLine: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dline')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		displayLine_cmd_val = self._cmd_group.get_repcap_cmd_value(displayLine, repcap.DisplayLine)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DLINe{displayLine_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
