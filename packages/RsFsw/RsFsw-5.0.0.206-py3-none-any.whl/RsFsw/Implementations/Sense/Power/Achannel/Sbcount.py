from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sbcount:
	"""Sbcount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sbcount", core, parent)

	def set(self, number: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SBCount \n
		Snippet: driver.sense.power.achannel.sbcount.set(number = 1.0) \n
		This command defines the number of sub blocks, i.e. groups of transmission channels in an MSR signal.
		For more information see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param number: Range: 1 to 8
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'SENSe:POWer:ACHannel:SBCount {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SBCount \n
		Snippet: value: float = driver.sense.power.achannel.sbcount.get() \n
		This command defines the number of sub blocks, i.e. groups of transmission channels in an MSR signal.
		For more information see 'Measurement on multi-standard radio (MSR) signals'. \n
			:return: number: Range: 1 to 8"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SBCount?')
		return Conversions.str_to_float(response)
