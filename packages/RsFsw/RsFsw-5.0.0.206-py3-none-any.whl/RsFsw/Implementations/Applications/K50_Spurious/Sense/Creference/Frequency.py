from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:CREFerence:FREQuency \n
		Snippet: driver.applications.k50Spurious.sense.creference.frequency.set(frequency = 1.0) \n
		Defines or queries the frequency at which the maximum peak of the signal, that is: the reference carrier, was found. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:CREFerence:FREQuency {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CREFerence:FREQuency \n
		Snippet: value: float = driver.applications.k50Spurious.sense.creference.frequency.get() \n
		Defines or queries the frequency at which the maximum peak of the signal, that is: the reference carrier, was found. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:CREFerence:FREQuency?')
		return Conversions.str_to_float(response)
