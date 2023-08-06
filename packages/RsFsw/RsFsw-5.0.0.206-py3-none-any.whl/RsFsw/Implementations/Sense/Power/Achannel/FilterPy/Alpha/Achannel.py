from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, alpha: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:ACHannel \n
		Snippet: driver.sense.power.achannel.filterPy.alpha.achannel.set(alpha = 1.0) \n
		This command defines the roll-off factor for the adjacent channel weighting filter. For asymmetrical MSR signals, this
		command defines the roll-off factor for the lower adjacent channel. To configure the factor for the upper adjacent
		channel, use the [SENSe:]POWer:ACHannel:FILTer:ALPHa:UACHannel command. \n
			:param alpha: Roll-off factor Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(alpha)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:ACHannel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:ACHannel \n
		Snippet: value: float = driver.sense.power.achannel.filterPy.alpha.achannel.get() \n
		This command defines the roll-off factor for the adjacent channel weighting filter. For asymmetrical MSR signals, this
		command defines the roll-off factor for the lower adjacent channel. To configure the factor for the upper adjacent
		channel, use the [SENSe:]POWer:ACHannel:FILTer:ALPHa:UACHannel command. \n
			:return: alpha: Roll-off factor Range: 0 to 1"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:ALPHa:ACHannel?')
		return Conversions.str_to_float(response)
