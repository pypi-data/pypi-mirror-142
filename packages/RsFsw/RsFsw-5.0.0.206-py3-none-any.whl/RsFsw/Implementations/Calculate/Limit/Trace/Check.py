from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Check:
	"""Check commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("check", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:TRACe<t>:CHECk \n
		Snippet: driver.calculate.limit.trace.check.set(state = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, trace = repcap.Trace.Default) \n
		This command turns the limit check for a specific trace on and off. To query the limit check result, use method RsFsw.
		Calculate.Limit.Fail.get_.
			INTRO_CMD_HELP: Note that this command replaces the two commands from previous signal and spectrum analyzers (which are still supported, however) : \n
			- CALCulate<n>:LIMit:TRACe<t>
			- method RsFsw.Calculate.Limit.State.set \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TRACe{trace_cmd_val}:CHECk {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:TRACe<t>:CHECk \n
		Snippet: value: bool = driver.calculate.limit.trace.check.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, trace = repcap.Trace.Default) \n
		This command turns the limit check for a specific trace on and off. To query the limit check result, use method RsFsw.
		Calculate.Limit.Fail.get_.
			INTRO_CMD_HELP: Note that this command replaces the two commands from previous signal and spectrum analyzers (which are still supported, however) : \n
			- CALCulate<n>:LIMit:TRACe<t>
			- method RsFsw.Calculate.Limit.State.set \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TRACe{trace_cmd_val}:CHECk?')
		return Conversions.str_to_bool(response)
