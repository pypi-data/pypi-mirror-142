from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsources:
	"""Nsources commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsources", core, parent)

	def set(self, input_sources: float) -> None:
		"""SCPI: CONFigure[:NR5G]:NSOurces \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.nsources.set(input_sources = 1.0) \n
		No command help available \n
			:param input_sources: No help available
		"""
		param = Conversions.decimal_value_to_str(input_sources)
		self._core.io.write(f'CONFigure:NR5G:NSOurces {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:NR5G]:NSOurces \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.nsources.get() \n
		No command help available \n
			:return: input_sources: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:NSOurces?')
		return Conversions.str_to_float(response)
