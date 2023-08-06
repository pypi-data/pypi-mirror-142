from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sinfo:
	"""Sinfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	def set(self, sequence_info: float) -> None:
		"""SCPI: CONFigure[:LTE]:DL:SINFo \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.sinfo.set(sequence_info = 1.0) \n
		No command help available \n
			:param sequence_info: No help available
		"""
		param = Conversions.decimal_value_to_str(sequence_info)
		self._core.io.write(f'CONFigure:LTE:DL:SINFo {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:DL:SINFo \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.sinfo.get() \n
		No command help available \n
			:return: sequence_info: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:DL:SINFo?')
		return Conversions.str_to_float(response)
