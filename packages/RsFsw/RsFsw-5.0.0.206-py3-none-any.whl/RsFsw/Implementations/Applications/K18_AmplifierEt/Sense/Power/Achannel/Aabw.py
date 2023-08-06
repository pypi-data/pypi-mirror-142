from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aabw:
	"""Aabw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aabw", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:AABW \n
		Snippet: driver.applications.k18AmplifierEt.sense.power.achannel.aabw.set(state = False) \n
		This command turns automatic selection of the measurement bandwidth for ACLR measurements on and off. When you turn this
		on, the application selects a measurement bandwidth that is large enough to capture all channels evaluated by the ACLR
		measurement. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:ACHannel:AABW {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:ACHannel:AABW \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.sense.power.achannel.aabw.get() \n
		This command turns automatic selection of the measurement bandwidth for ACLR measurements on and off. When you turn this
		on, the application selects a measurement bandwidth that is large enough to capture all channels evaluated by the ACLR
		measurement. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:AABW?')
		return Conversions.str_to_bool(response)
