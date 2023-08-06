from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.Types import DataType
from ...........Internal.ArgSingleList import ArgSingleList
from ...........Internal.ArgSingle import ArgSingle
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, sb_gaps: enums.SubBlockGaps, state: bool, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:GCHannel[:STATe]:GAP<gap>:MANual:UPPer \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.gchannel.state.gap.manual.upper.set(sb_gaps = enums.SubBlockGaps.AB, state = False, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param sb_gaps: No help available
			:param state: No help available
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sb_gaps', sb_gaps, DataType.Enum, enums.SubBlockGaps), ArgSingle('state', state, DataType.Boolean))
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:GCHannel:STATe:GAP{gapChannel_cmd_val}:MANual:UPPer {param}'.rstrip())

	def get(self, sb_gaps: enums.SubBlockGaps, gapChannel=repcap.GapChannel.Default) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:GCHannel[:STATe]:GAP<gap>:MANual:UPPer \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.power.achannel.gchannel.state.gap.manual.upper.get(sb_gaps = enums.SubBlockGaps.AB, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param sb_gaps: No help available
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: state: No help available"""
		param = Conversions.enum_scalar_to_str(sb_gaps, enums.SubBlockGaps)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:GCHannel:STATe:GAP{gapChannel_cmd_val}:MANual:UPPer? {param}')
		return Conversions.str_to_bool(response)
