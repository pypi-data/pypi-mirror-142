from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pindex:
	"""Pindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pindex", core, parent)

	def set(self, prb_index: float) -> None:
		"""SCPI: CONFigure[:LTE]:DL:PINDex \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.pindex.set(prb_index = 1.0) \n
		No command help available \n
			:param prb_index: No help available
		"""
		param = Conversions.decimal_value_to_str(prb_index)
		self._core.io.write(f'CONFigure:LTE:DL:PINDex {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:LTE]:DL:PINDex \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.pindex.get() \n
		No command help available \n
			:return: prb_index: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:DL:PINDex?')
		return Conversions.str_to_float(response)
