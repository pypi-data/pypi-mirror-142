from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, value: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:ACHannel \n
		Snippet: driver.applications.k18AmplifierEt.sense.power.achannel.filterPy.state.achannel.set(value = False) \n
		This command turns the weighting filter for the adjacent channel on and off. \n
			:param value: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(value)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:STATe:ACHannel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer[:STATe]:ACHannel \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.power.achannel.filterPy.state.achannel.get() \n
		This command turns the weighting filter for the adjacent channel on and off. \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:STATe:ACHannel?')
		return Conversions.str_to_bool(response)
