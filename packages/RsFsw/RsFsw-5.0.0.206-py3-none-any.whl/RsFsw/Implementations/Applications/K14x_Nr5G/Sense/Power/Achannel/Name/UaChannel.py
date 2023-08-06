from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UaChannel:
	"""UaChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uaChannel", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:UACHannel \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.name.uaChannel.set(name = '1') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:POWer:ACHannel:NAME:UACHannel {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:UACHannel \n
		Snippet: value: str = driver.applications.k14Xnr5G.sense.power.achannel.name.uaChannel.get() \n
		No command help available \n
			:return: name: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:NAME:UACHannel?')
		return trim_str_response(response)
