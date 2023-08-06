from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.Types import DataType
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, sb_gaps: enums.SubBlockGaps, state: bool, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:MANual:UPPer:ACLR[:RELative]:STATe \n
		Snippet: driver.calculate.limit.acPower.gap.manual.upper.aclr.relative.state.set(sb_gaps = enums.SubBlockGaps.AB, state = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		This command turns the relative limit check for the specified upper gap (CACLR) channel on and off. You have to activate
		the general ACLR limit check before using this command with method RsFsw.Calculate.Limit.AcPower.State.set. This command
		is only available for for asymmetrical (manual) configuration of gap channels (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param sb_gaps: AB | BC | CD | DE | EF | FG | GH Name of the gap, defined by the letters of the surrounding sub blocks (e.g. 'AB' for the gap between sub blocks A and B) .
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sb_gaps', sb_gaps, DataType.Enum, enums.SubBlockGaps), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:MANual:UPPer:ACLR:RELative:STATe {param}'.rstrip())

	def get(self, sb_gaps: enums.SubBlockGaps, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:MANual:UPPer:ACLR[:RELative]:STATe \n
		Snippet: value: bool = driver.calculate.limit.acPower.gap.manual.upper.aclr.relative.state.get(sb_gaps = enums.SubBlockGaps.AB, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		This command turns the relative limit check for the specified upper gap (CACLR) channel on and off. You have to activate
		the general ACLR limit check before using this command with method RsFsw.Calculate.Limit.AcPower.State.set. This command
		is only available for for asymmetrical (manual) configuration of gap channels (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param sb_gaps: AB | BC | CD | DE | EF | FG | GH Name of the gap, defined by the letters of the surrounding sub blocks (e.g. 'AB' for the gap between sub blocks A and B) .
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		param = Conversions.enum_scalar_to_str(sb_gaps, enums.SubBlockGaps)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:MANual:UPPer:ACLR:RELative:STATe? {param}')
		return Conversions.str_to_bool(response)
