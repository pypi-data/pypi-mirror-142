from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:NPRatio:CHANnel:INTegration:BWIDth \n
		Snippet: driver.sense.npratio.channel.integration.bandwidth.set(frequency = 1.0) \n
		Defines the bandwidth to be used for total power calculation as an absolute value. This value is only considered for
		[SENSe:]NPRatio:CHANnel:INTegration:AUTOOFF. The entire specified bandwidth is used, including any defined notches. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:NPRatio:CHANnel:INTegration:BWIDth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NPRatio:CHANnel:INTegration:BWIDth \n
		Snippet: value: float = driver.sense.npratio.channel.integration.bandwidth.get() \n
		Defines the bandwidth to be used for total power calculation as an absolute value. This value is only considered for
		[SENSe:]NPRatio:CHANnel:INTegration:AUTOOFF. The entire specified bandwidth is used, including any defined notches. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:NPRatio:CHANnel:INTegration:BWIDth?')
		return Conversions.str_to_float(response)
