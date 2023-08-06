from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, eutra_center_frequency: float) -> None:
		"""SCPI: CONFigure[:LTE]:EUTRa:FREQuency \n
		Snippet: driver.applications.k10Xlte.configure.lte.eutra.frequency.set(eutra_center_frequency = 1.0) \n
		No command help available \n
			:param eutra_center_frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(eutra_center_frequency)
		self._core.io.write(f'CONFigure:LTE:EUTRa:FREQuency {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:EUTRa:FREQuency \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.eutra.frequency.get() \n
		No command help available \n
			:return: eutra_center_frequency: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:EUTRa:FREQuency?')
		return Conversions.str_to_float(response)
