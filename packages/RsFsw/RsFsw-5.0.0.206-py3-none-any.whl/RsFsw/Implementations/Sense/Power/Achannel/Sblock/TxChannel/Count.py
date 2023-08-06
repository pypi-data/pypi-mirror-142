from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, number: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:TXCHannel:COUNt \n
		Snippet: driver.sense.power.achannel.sblock.txChannel.count.set(number = 1.0, subBlock = repcap.SubBlock.Default) \n
		This command defines the number of transmission channels the specific sub block contains. This command is for MSR signals
		only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For details on MSR signals see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param number: Range: 1 to 18
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
		"""
		param = Conversions.decimal_value_to_str(number)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:TXCHannel:COUNt {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:TXCHannel:COUNt \n
		Snippet: value: float = driver.sense.power.achannel.sblock.txChannel.count.get(subBlock = repcap.SubBlock.Default) \n
		This command defines the number of transmission channels the specific sub block contains. This command is for MSR signals
		only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For details on MSR signals see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:return: number: Range: 1 to 18"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:TXCHannel:COUNt?')
		return Conversions.str_to_float(response)
