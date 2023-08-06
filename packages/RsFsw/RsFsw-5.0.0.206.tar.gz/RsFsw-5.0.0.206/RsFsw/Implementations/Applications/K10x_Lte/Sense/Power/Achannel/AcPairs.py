from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcPairs:
	"""AcPairs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acPairs", core, parent)

	def set(self, channel_pairs: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:ACPairs \n
		Snippet: driver.applications.k10Xlte.sense.power.achannel.acPairs.set(channel_pairs = 1.0) \n
		No command help available \n
			:param channel_pairs: No help available
		"""
		param = Conversions.decimal_value_to_str(channel_pairs)
		self._core.io.write(f'SENSe:POWer:ACHannel:ACPairs {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:ACPairs \n
		Snippet: value: float = driver.applications.k10Xlte.sense.power.achannel.acPairs.get() \n
		No command help available \n
			:return: channel_pairs: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:ACPairs?')
		return Conversions.str_to_float(response)
