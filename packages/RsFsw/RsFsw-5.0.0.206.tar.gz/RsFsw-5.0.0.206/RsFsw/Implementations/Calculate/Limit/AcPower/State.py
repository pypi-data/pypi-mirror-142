from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower[:STATe] \n
		Snippet: driver.calculate.limit.acPower.state.set(state = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command turns the limit check for ACLR measurements on and off. In addition, limits must be defined and activated
		individually for each channel (see method RsFsw.Calculate.Limit.AcPower.Achannel.Relative.State.set, method RsFsw.
		Calculate.Limit.AcPower.Alternate.Relative.State.set, method RsFsw.Calculate.Limit.AcPower.Gap.Auto.Absolute.State.set,
		method RsFsw.Calculate.Limit.AcPower.Gap.Auto.Aclr.Relative.State.set and method RsFsw.Calculate.Limit.AcPower.Gap.Auto.
		Caclr.Relative.State.set) . \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:STATe {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower[:STATe] \n
		Snippet: value: bool = driver.calculate.limit.acPower.state.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command turns the limit check for ACLR measurements on and off. In addition, limits must be defined and activated
		individually for each channel (see method RsFsw.Calculate.Limit.AcPower.Achannel.Relative.State.set, method RsFsw.
		Calculate.Limit.AcPower.Alternate.Relative.State.set, method RsFsw.Calculate.Limit.AcPower.Gap.Auto.Absolute.State.set,
		method RsFsw.Calculate.Limit.AcPower.Gap.Auto.Aclr.Relative.State.set and method RsFsw.Calculate.Limit.AcPower.Gap.Auto.
		Caclr.Relative.State.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:STATe?')
		return Conversions.str_to_bool(response)
