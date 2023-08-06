from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:ACHannel \n
		Snippet: driver.sense.power.achannel.name.achannel.set(name = '1') \n
		This command defines a name for the adjacent channel. For MSR ACLR measurements, this command defines the name for the
		lower adjacent channel in asymmetric channel definitions. To define the name for the upper adjacent channel use the
		[SENSe:]POWer:ACHannel:NAME:UACHannel command. For details on MSR signals see 'Measurement on multi-standard radio (MSR)
		signals'. \n
			:param name: String containing the name of the channel
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:POWer:ACHannel:NAME:ACHannel {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:ACHannel \n
		Snippet: value: str = driver.sense.power.achannel.name.achannel.get() \n
		This command defines a name for the adjacent channel. For MSR ACLR measurements, this command defines the name for the
		lower adjacent channel in asymmetric channel definitions. To define the name for the upper adjacent channel use the
		[SENSe:]POWer:ACHannel:NAME:UACHannel command. For details on MSR signals see 'Measurement on multi-standard radio (MSR)
		signals'. \n
			:return: name: String containing the name of the channel"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:NAME:ACHannel?')
		return trim_str_response(response)
