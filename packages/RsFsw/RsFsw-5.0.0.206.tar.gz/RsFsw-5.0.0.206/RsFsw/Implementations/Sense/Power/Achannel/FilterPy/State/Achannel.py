from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:ACHannel \n
		Snippet: driver.sense.power.achannel.filterPy.state.achannel.set(state = False) \n
		This command turns the weighting filter for the adjacent channel on and off. For asymmetrical MSR signals, this command
		turns the weighting filter for the lower adjacent channel on and off. To configure the filter state for the upper
		adjacent channel, use the [SENSe:]POWer:ACHannel:FILTer[:STATe]:UACHannel command. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:STATe:ACHannel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:ACHannel \n
		Snippet: value: bool = driver.sense.power.achannel.filterPy.state.achannel.get() \n
		This command turns the weighting filter for the adjacent channel on and off. For asymmetrical MSR signals, this command
		turns the weighting filter for the lower adjacent channel on and off. To configure the filter state for the upper
		adjacent channel, use the [SENSe:]POWer:ACHannel:FILTer[:STATe]:UACHannel command. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:STATe:ACHannel?')
		return Conversions.str_to_bool(response)
