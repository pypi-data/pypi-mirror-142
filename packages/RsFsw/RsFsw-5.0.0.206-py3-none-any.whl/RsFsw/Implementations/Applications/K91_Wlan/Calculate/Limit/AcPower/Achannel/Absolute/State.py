from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state_lower: bool, state_upper: bool = None, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel:ABSolute:STATe \n
		Snippet: driver.applications.k91Wlan.calculate.limit.acPower.achannel.absolute.state.set(state_lower = False, state_upper = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param state_lower: No help available
			:param state_upper: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state_lower', state_lower, DataType.Boolean), ArgSingle('state_upper', state_upper, DataType.Boolean, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:ABSolute:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class State(StructBase):
		"""Response structure. Fields: \n
			- State_Lower: bool: No parameter help available
			- State_Upper: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State_Lower'),
			ArgStruct.scalar_bool('State_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State_Lower: bool = None
			self.State_Upper: bool = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> State:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel:ABSolute:STATe \n
		Snippet: value: State = driver.applications.k91Wlan.calculate.limit.acPower.achannel.absolute.state.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for State structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:ABSolute:STATe?', self.__class__.State())
