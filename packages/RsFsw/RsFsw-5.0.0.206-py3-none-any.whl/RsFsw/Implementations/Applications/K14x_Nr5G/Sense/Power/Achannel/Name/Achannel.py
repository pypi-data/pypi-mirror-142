from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:ACHannel \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.name.achannel.set(name = '1') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:POWer:ACHannel:NAME:ACHannel {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:ACHannel \n
		Snippet: value: str = driver.applications.k14Xnr5G.sense.power.achannel.name.achannel.get() \n
		No command help available \n
			:return: name: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:NAME:ACHannel?')
		return trim_str_response(response)
