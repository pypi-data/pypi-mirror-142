from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msize:
	"""Msize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msize", core, parent)

	def set(self, bandwidth: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>[:AUTO]:MSIZe \n
		Snippet: driver.sense.power.achannel.gap.auto.msize.set(bandwidth = 1.0, gapChannel = repcap.GapChannel.Default) \n
		If the gap between the sub blocks does not exceed the specified bandwidth, the gap channels are not displayed in the
		diagram, and the gap channel results are not calculated in the result summary. This command is only available for
		symmetrical gap channels in 'Auto' gap mode (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param bandwidth: numeric value in Hz Unit: Hz
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:AUTO:MSIZe {param}')

	def get(self, gapChannel=repcap.GapChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>[:AUTO]:MSIZe \n
		Snippet: value: float = driver.sense.power.achannel.gap.auto.msize.get(gapChannel = repcap.GapChannel.Default) \n
		If the gap between the sub blocks does not exceed the specified bandwidth, the gap channels are not displayed in the
		diagram, and the gap channel results are not calculated in the result summary. This command is only available for
		symmetrical gap channels in 'Auto' gap mode (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: bandwidth: numeric value in Hz Unit: Hz"""
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:AUTO:MSIZe?')
		return Conversions.str_to_float(response)
