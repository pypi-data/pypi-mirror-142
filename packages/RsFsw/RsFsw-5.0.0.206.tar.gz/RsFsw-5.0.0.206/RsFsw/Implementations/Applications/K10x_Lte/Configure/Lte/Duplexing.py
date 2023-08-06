from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duplexing:
	"""Duplexing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duplexing", core, parent)

	def set(self, duplexing: enums.DuplexingLte) -> None:
		"""SCPI: CONFigure[:LTE]:DUPLexing \n
		Snippet: driver.applications.k10Xlte.configure.lte.duplexing.set(duplexing = enums.DuplexingLte.FDD) \n
		This command selects the duplexing mode. \n
			:param duplexing: TDD Time division duplex FDD Frequency division duplex
		"""
		param = Conversions.enum_scalar_to_str(duplexing, enums.DuplexingLte)
		self._core.io.write(f'CONFigure:LTE:DUPLexing {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DuplexingLte:
		"""SCPI: CONFigure[:LTE]:DUPLexing \n
		Snippet: value: enums.DuplexingLte = driver.applications.k10Xlte.configure.lte.duplexing.get() \n
		This command selects the duplexing mode. \n
			:return: duplexing: TDD Time division duplex FDD Frequency division duplex"""
		response = self._core.io.query_str(f'CONFigure:LTE:DUPLexing?')
		return Conversions.str_to_scalar_enum(response, enums.DuplexingLte)
