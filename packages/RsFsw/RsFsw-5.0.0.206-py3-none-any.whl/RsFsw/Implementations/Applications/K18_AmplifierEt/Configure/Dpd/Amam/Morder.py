from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Morder:
	"""Morder commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("morder", core, parent)

	def set(self, am_am_max_order: float) -> None:
		"""SCPI: CONFigure:DPD:AMAM:MORDer \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.amam.morder.set(am_am_max_order = 1.0) \n
		No command help available \n
			:param am_am_max_order: No help available
		"""
		param = Conversions.decimal_value_to_str(am_am_max_order)
		self._core.io.write(f'CONFigure:DPD:AMAM:MORDer {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:DPD:AMAM:MORDer \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.dpd.amam.morder.get() \n
		No command help available \n
			:return: am_am_max_order: No help available"""
		response = self._core.io.query_str(f'CONFigure:DPD:AMAM:MORDer?')
		return Conversions.str_to_float(response)
