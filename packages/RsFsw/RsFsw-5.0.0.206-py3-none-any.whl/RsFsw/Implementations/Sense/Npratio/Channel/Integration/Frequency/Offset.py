from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:NPRatio:CHANnel:INTegration:FREQuency:OFFSet \n
		Snippet: driver.sense.npratio.channel.integration.frequency.offset.set(frequency = 1.0) \n
		Shifts the bandwidth to be used for total power density calculation away from the currently defined center frequency. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:NPRatio:CHANnel:INTegration:FREQuency:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:NPRatio:CHANnel:INTegration:FREQuency:OFFSet \n
		Snippet: value: float = driver.sense.npratio.channel.integration.frequency.offset.get() \n
		Shifts the bandwidth to be used for total power density calculation away from the currently defined center frequency. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:NPRatio:CHANnel:INTegration:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)
