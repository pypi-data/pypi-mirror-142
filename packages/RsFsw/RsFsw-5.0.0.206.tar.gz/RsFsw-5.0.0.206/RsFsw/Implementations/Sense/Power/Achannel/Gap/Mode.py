from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AutoManualMode, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>:MODE \n
		Snippet: driver.sense.power.achannel.gap.mode.set(mode = enums.AutoManualMode.AUTO, gapChannel = repcap.GapChannel.Default) \n
		Defines how gap channels are configured. \n
			:param mode: AUTO | MANual AUTO In 'Auto' mode, upper and lower gap channels are configured identically, so only two channels need to be configured (gap 1, gap 2) . Gap channels are configured identically for all gaps, if more than two sub blocks are defined. Depending on the defined minimum gap size, the actual number of evaluated gap channels is determined automatically. See also [SENSe:]POWer:ACHannel:GAPgap[:AUTO]:MSIZe. MANual In 'Manual' mode, up to four channels can be configured individually for each gap. Active gap channels are always evaluated, regardless of the gap size. See also [SENSe:]POWer:ACHannel:GCHannel[:STATe]:GAPgap:MANual:LOWer and [SENSe:]POWer:ACHannel:GCHannel[:STATe]:GAPgap:MANual:UPPer.
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, gapChannel=repcap.GapChannel.Default) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>:MODE \n
		Snippet: value: enums.AutoManualMode = driver.sense.power.achannel.gap.mode.get(gapChannel = repcap.GapChannel.Default) \n
		Defines how gap channels are configured. \n
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: mode: AUTO | MANual AUTO In 'Auto' mode, upper and lower gap channels are configured identically, so only two channels need to be configured (gap 1, gap 2) . Gap channels are configured identically for all gaps, if more than two sub blocks are defined. Depending on the defined minimum gap size, the actual number of evaluated gap channels is determined automatically. See also [SENSe:]POWer:ACHannel:GAPgap[:AUTO]:MSIZe. MANual In 'Manual' mode, up to four channels can be configured individually for each gap. Active gap channels are always evaluated, regardless of the gap size. See also [SENSe:]POWer:ACHannel:GCHannel[:STATe]:GAPgap:MANual:LOWer and [SENSe:]POWer:ACHannel:GCHannel[:STATe]:GAPgap:MANual:UPPer."""
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
