from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:ACHannel \n
		Snippet: driver.sense.power.achannel.bandwidth.achannel.set(bandwidth = 1.0) \n
		This command defines the channel bandwidth of the adjacent channels. The adjacent channels are the first channels to the
		left and right of the transmission channels. If you set the channel bandwidth for these channels, the R&S FSW sets the
		bandwidth of the alternate channels to the same value (not for MSR signals) . For asymmetrical MSR signals, this command
		defines the bandwidth of the lower adjacent channel. To configure the bandwidth for the upper adjacent channel, use the
		[SENSe:]POWer:ACHannel:BANDwidth:UACHannel command. Steep-edged channel filters are available for fast ACLR measurements. \n
			:param bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:ACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:ACHannel \n
		Snippet: value: float = driver.sense.power.achannel.bandwidth.achannel.get() \n
		This command defines the channel bandwidth of the adjacent channels. The adjacent channels are the first channels to the
		left and right of the transmission channels. If you set the channel bandwidth for these channels, the R&S FSW sets the
		bandwidth of the alternate channels to the same value (not for MSR signals) . For asymmetrical MSR signals, this command
		defines the bandwidth of the lower adjacent channel. To configure the bandwidth for the upper adjacent channel, use the
		[SENSe:]POWer:ACHannel:BANDwidth:UACHannel command. Steep-edged channel filters are available for fast ACLR measurements. \n
			:return: bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:ACHannel?')
		return Conversions.str_to_float(response)
