from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ppow:
	"""Ppow commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ppow", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:POWer:PPOW \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.generator.power.ppow.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:POWer:PPOW?')
		return Conversions.str_to_float(response)
