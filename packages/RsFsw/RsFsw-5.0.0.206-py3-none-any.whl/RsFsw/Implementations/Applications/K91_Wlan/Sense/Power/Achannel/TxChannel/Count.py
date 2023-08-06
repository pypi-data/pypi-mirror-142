from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, number: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:TXCHannel:COUNt \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.txChannel.count.set(number = 1.0) \n
		No command help available \n
			:param number: No help available
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'SENSe:POWer:ACHannel:TXCHannel:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:TXCHannel:COUNt \n
		Snippet: value: float = driver.applications.k91Wlan.sense.power.achannel.txChannel.count.get() \n
		No command help available \n
			:return: number: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:TXCHannel:COUNt?')
		return Conversions.str_to_float(response)
