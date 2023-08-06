from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaChannel:
	"""UaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaChannel", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:UACHannel \n
		Snippet: driver.sense.power.achannel.bandwidth.uaChannel.set(bandwidth = 1.0) \n
		This command defines the channel bandwidth of the upper adjacent channel in asymmetrical configurations. The adjacent
		channel is the first pair of channels next to the transmission channels. To configure the bandwidth for the lower
		adjacent channel, use the [SENSe:]POWer:ACHannel:BANDwidth:ACHannel command. Steep-edged channel filters are available
		for fast ACLR measurements. \n
			:param bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:UACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:UACHannel \n
		Snippet: value: float = driver.sense.power.achannel.bandwidth.uaChannel.get() \n
		This command defines the channel bandwidth of the upper adjacent channel in asymmetrical configurations. The adjacent
		channel is the first pair of channels next to the transmission channels. To configure the bandwidth for the lower
		adjacent channel, use the [SENSe:]POWer:ACHannel:BANDwidth:ACHannel command. Steep-edged channel filters are available
		for fast ACLR measurements. \n
			:return: bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:UACHannel?')
		return Conversions.str_to_float(response)
