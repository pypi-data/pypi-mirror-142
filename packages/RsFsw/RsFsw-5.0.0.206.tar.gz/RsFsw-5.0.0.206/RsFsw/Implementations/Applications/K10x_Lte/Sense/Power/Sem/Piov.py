from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Piov:
	"""Piov commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("piov", core, parent)

	def set(self, scaling: float) -> None:
		"""SCPI: [SENSe]:POWer:SEM:PIOV \n
		Snippet: driver.applications.k10Xlte.sense.power.sem.piov.set(scaling = 1.0) \n
		No command help available \n
			:param scaling: No help available
		"""
		param = Conversions.decimal_value_to_str(scaling)
		self._core.io.write(f'SENSe:POWer:SEM:PIOV {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:SEM:PIOV \n
		Snippet: value: float = driver.applications.k10Xlte.sense.power.sem.piov.get() \n
		No command help available \n
			:return: scaling: No help available"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:PIOV?')
		return Conversions.str_to_float(response)
