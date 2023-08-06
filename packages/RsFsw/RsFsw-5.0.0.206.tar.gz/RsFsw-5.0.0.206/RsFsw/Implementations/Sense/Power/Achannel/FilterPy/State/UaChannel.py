from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaChannel:
	"""UaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaChannel", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:UACHannel \n
		Snippet: driver.sense.power.achannel.filterPy.state.uaChannel.set(state = False) \n
		This command turns the weighting filter for the upper adjacent channel on and off for asymmetrical MSR signals.
		To configure the factor for the lower adjacent channel, use the [SENSe:]POWer:ACHannel:FILTer[:STATe]:ACHannel command. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:STATe:UACHannel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:UACHannel \n
		Snippet: value: bool = driver.sense.power.achannel.filterPy.state.uaChannel.get() \n
		This command turns the weighting filter for the upper adjacent channel on and off for asymmetrical MSR signals.
		To configure the factor for the lower adjacent channel, use the [SENSe:]POWer:ACHannel:FILTer[:STATe]:ACHannel command. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:STATe:UACHannel?')
		return Conversions.str_to_bool(response)
