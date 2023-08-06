from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msize:
	"""Msize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msize", core, parent)

	def set(self, bandwidth: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>:MSIZe \n
		Snippet: driver.applications.k10Xlte.sense.power.achannel.gap.msize.set(bandwidth = 1.0, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param bandwidth: No help available
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:MSIZe {param}')

	def get(self, gapChannel=repcap.GapChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:GAP<gap>:MSIZe \n
		Snippet: value: float = driver.applications.k10Xlte.sense.power.achannel.gap.msize.get(gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: bandwidth: No help available"""
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:GAP{gapChannel_cmd_val}:MSIZe?')
		return Conversions.str_to_float(response)
