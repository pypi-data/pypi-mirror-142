from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaChannel:
	"""UaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaChannel", core, parent)

	def set(self, alpha: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:UACHannel \n
		Snippet: driver.sense.power.achannel.filterPy.alpha.uaChannel.set(alpha = 1.0) \n
		This command defines the roll-off factor for the upper adjacent channel weighting filter for asymmetrical MSR signals. To
		configure the factor for the upper adjacent channel, use the [SENSe:]POWer:ACHannel:FILTer:ALPHa:ACHannel command. \n
			:param alpha: Roll-off factor Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(alpha)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:UACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:UACHannel \n
		Snippet: value: float = driver.sense.power.achannel.filterPy.alpha.uaChannel.get() \n
		This command defines the roll-off factor for the upper adjacent channel weighting filter for asymmetrical MSR signals. To
		configure the factor for the upper adjacent channel, use the [SENSe:]POWer:ACHannel:FILTer:ALPHa:ACHannel command. \n
			:return: alpha: Roll-off factor Range: 0 to 1"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:ALPHa:UACHannel?')
		return Conversions.str_to_float(response)
