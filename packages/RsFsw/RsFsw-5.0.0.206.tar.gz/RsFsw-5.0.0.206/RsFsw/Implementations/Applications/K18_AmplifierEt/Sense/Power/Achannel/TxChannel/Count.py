from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:TXCHannel:COUNt \n
		Snippet: driver.applications.k18AmplifierEt.sense.power.achannel.txChannel.count.set(count = 1.0) \n
		This command defines the number of transmission channels. The command works for measurements in the frequency domain. \n
			:param count: Range: 1 to 18
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:POWer:ACHannel:TXCHannel:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:TXCHannel:COUNt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.power.achannel.txChannel.count.get() \n
		This command defines the number of transmission channels. The command works for measurements in the frequency domain. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:TXCHannel:COUNt?')
		return Conversions.str_to_float(response)
