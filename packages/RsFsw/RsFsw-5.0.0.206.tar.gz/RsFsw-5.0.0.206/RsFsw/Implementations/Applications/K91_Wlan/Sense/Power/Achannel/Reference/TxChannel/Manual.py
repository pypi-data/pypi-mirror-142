from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Manual:
	"""Manual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("manual", core, parent)

	def set(self, channel_number: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:REFerence:TXCHannel:MANual \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.reference.txChannel.manual.set(channel_number = 1.0) \n
		No command help available \n
			:param channel_number: No help available
		"""
		param = Conversions.decimal_value_to_str(channel_number)
		self._core.io.write(f'SENSe:POWer:ACHannel:REFerence:TXCHannel:MANual {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:REFerence:TXCHannel:MANual \n
		Snippet: value: float = driver.applications.k91Wlan.sense.power.achannel.reference.txChannel.manual.get() \n
		No command help available \n
			:return: channel_number: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:REFerence:TXCHannel:MANual?')
		return Conversions.str_to_float(response)
