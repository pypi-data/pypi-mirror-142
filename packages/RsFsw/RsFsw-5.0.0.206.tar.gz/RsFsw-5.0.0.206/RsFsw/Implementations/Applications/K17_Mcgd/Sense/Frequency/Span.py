from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Span:
	"""Span commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("span", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:SPAN \n
		Snippet: driver.applications.k17Mcgd.sense.frequency.span.set(frequency = 1.0) \n
		No command help available \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:SPAN {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:SPAN \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.frequency.span.get() \n
		No command help available \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:SPAN?')
		return Conversions.str_to_float(response)
