from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upper:
	"""Upper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upper", core, parent)

	def set(self, sb_gaps: enums.SubBlockGaps, bandwidth: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:GAP<gap>:MANual:UPPer \n
		Snippet: driver.sense.power.achannel.bandwidth.gap.manual.upper.set(sb_gaps = enums.SubBlockGaps.AB, bandwidth = 1.0, gapChannel = repcap.GapChannel.Default) \n
		Defines the bandwidth of the upper gap channel in the specified gap. This command is only available for for asymmetrical
		(manual) configuration of gap channels (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param sb_gaps: AB | BC | CD | DE | EF | FG | GH Name of the gap, defined by the letters of the surrounding sub blocks (e.g. 'AB' for the gap between sub blocks A and B) .
			:param bandwidth: Unit: HZ
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sb_gaps', sb_gaps, DataType.Enum, enums.SubBlockGaps), ArgSingle('bandwidth', bandwidth, DataType.Float))
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:GAP{gapChannel_cmd_val}:MANual:UPPer {param}'.rstrip())

	def get(self, sb_gaps: enums.SubBlockGaps, gapChannel=repcap.GapChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:GAP<gap>:MANual:UPPer \n
		Snippet: value: float = driver.sense.power.achannel.bandwidth.gap.manual.upper.get(sb_gaps = enums.SubBlockGaps.AB, gapChannel = repcap.GapChannel.Default) \n
		Defines the bandwidth of the upper gap channel in the specified gap. This command is only available for for asymmetrical
		(manual) configuration of gap channels (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param sb_gaps: AB | BC | CD | DE | EF | FG | GH Name of the gap, defined by the letters of the surrounding sub blocks (e.g. 'AB' for the gap between sub blocks A and B) .
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: bandwidth: Unit: HZ"""
		param = Conversions.enum_scalar_to_str(sb_gaps, enums.SubBlockGaps)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:GAP{gapChannel_cmd_val}:MANual:UPPer? {param}')
		return Conversions.str_to_float(response)
