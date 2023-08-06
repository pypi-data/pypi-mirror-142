from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TABLe:EMODel:RTPTime:LIMit:STATe \n
		Snippet: driver.applications.k6Pulse.calculate.table.emodel.riseTopPoint.time.limit.state.set(state = False, window = repcap.Window.Default) \n
		Activates or deactivates a limit check for the selected parameter.
		The limits are defined using CALCulate<n>:TABLe:<ParameterGroup>:<Parameter>:LIMit. Commands for the parameter group
		<TSIDelobe> are only available if the additional option R&S FSW-K6S is installed. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TABLe:EMODel:RTPTime:LIMit:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:TABLe:EMODel:RTPTime:LIMit:STATe \n
		Snippet: value: bool = driver.applications.k6Pulse.calculate.table.emodel.riseTopPoint.time.limit.state.get(window = repcap.Window.Default) \n
		Activates or deactivates a limit check for the selected parameter.
		The limits are defined using CALCulate<n>:TABLe:<ParameterGroup>:<Parameter>:LIMit. Commands for the parameter group
		<TSIDelobe> are only available if the additional option R&S FSW-K6S is installed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TABLe:EMODel:RTPTime:LIMit:STATe?')
		return Conversions.str_to_bool(response)
