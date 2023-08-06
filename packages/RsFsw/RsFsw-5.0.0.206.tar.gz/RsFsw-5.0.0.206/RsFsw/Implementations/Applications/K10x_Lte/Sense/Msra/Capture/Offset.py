from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: [SENSe]:MSRA:CAPTure:OFFSet \n
		Snippet: driver.applications.k10Xlte.sense.msra.capture.offset.set(offset = 1.0) \n
		No command help available \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SENSe:MSRA:CAPTure:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MSRA:CAPTure:OFFSet \n
		Snippet: value: float = driver.applications.k10Xlte.sense.msra.capture.offset.get() \n
		No command help available \n
			:return: offset: No help available"""
		response = self._core.io.query_str(f'SENSe:MSRA:CAPTure:OFFSet?')
		return Conversions.str_to_float(response)
