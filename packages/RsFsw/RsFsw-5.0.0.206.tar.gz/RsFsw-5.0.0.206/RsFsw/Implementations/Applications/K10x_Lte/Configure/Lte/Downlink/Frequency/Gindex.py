from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gindex:
	"""Gindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gindex", core, parent)

	def set(self, freq_offset_to_eutra: float) -> None:
		"""SCPI: CONFigure[:LTE]:DL:FREQuency:GINDex \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.frequency.gindex.set(freq_offset_to_eutra = 1.0) \n
		No command help available \n
			:param freq_offset_to_eutra: No help available
		"""
		param = Conversions.decimal_value_to_str(freq_offset_to_eutra)
		self._core.io.write(f'CONFigure:LTE:DL:FREQuency:GINDex {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:DL:FREQuency:GINDex \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.frequency.gindex.get() \n
		No command help available \n
			:return: freq_offset_to_eutra: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:DL:FREQuency:GINDex?')
		return Conversions.str_to_float(response)
