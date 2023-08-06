from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lower:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, sb_gaps: enums.SubBlockGaps, count: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>:MANual:CHANnel:COUNt:LOWer \n
		Snippet: driver.sense.power.achannel.gap.manual.channel.count.lower.set(sb_gaps = enums.SubBlockGaps.AB, count = 1.0, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param sb_gaps: No help available
			:param count: No help available
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sb_gaps', sb_gaps, DataType.Enum, enums.SubBlockGaps), ArgSingle('count', count, DataType.Float))
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:MANual:CHANnel:COUNt:LOWer {param}'.rstrip())

	def get(self, sb_gaps: enums.SubBlockGaps, gapChannel=repcap.GapChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>:MANual:CHANnel:COUNt:LOWer \n
		Snippet: value: float = driver.sense.power.achannel.gap.manual.channel.count.lower.get(sb_gaps = enums.SubBlockGaps.AB, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param sb_gaps: No help available
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: count: No help available"""
		param = Conversions.enum_scalar_to_str(sb_gaps, enums.SubBlockGaps)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:MANual:CHANnel:COUNt:LOWer? {param}')
		return Conversions.str_to_float(response)
