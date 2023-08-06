from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, period: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:BBPower:HOLDoff \n
		Snippet: driver.applications.k10Xlte.trigger.sequence.bbPower.holdoff.set(period = 1.0) \n
		No command help available \n
			:param period: No help available
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'TRIGger:SEQuence:BBPower:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:BBPower:HOLDoff \n
		Snippet: value: float = driver.applications.k10Xlte.trigger.sequence.bbPower.holdoff.get() \n
		No command help available \n
			:return: period: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:BBPower:HOLDoff?')
		return Conversions.str_to_float(response)
