from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ldirection:
	"""Ldirection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ldirection", core, parent)

	def set(self, mode: enums.DlUlDirection) -> None:
		"""SCPI: CONFigure[:NR5G]:LDIRection \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.ldirection.set(mode = enums.DlUlDirection.DL) \n
		This command selects the link direction you want to analyze. \n
			:param mode: DL Selects the downlink application to analyze 5G NR downlink signals. Requires option R&S FSW-K144. UL Selects the uplink application to analyze 5G NR uplink signals. Requires option R&S FSW-K145.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.DlUlDirection)
		self._core.io.write(f'CONFigure:NR5G:LDIRection {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DlUlDirection:
		"""SCPI: CONFigure[:NR5G]:LDIRection \n
		Snippet: value: enums.DlUlDirection = driver.applications.k14Xnr5G.configure.nr5G.ldirection.get() \n
		This command selects the link direction you want to analyze. \n
			:return: mode: DL Selects the downlink application to analyze 5G NR downlink signals. Requires option R&S FSW-K144. UL Selects the uplink application to analyze 5G NR uplink signals. Requires option R&S FSW-K145."""
		response = self._core.io.query_str(f'CONFigure:NR5G:LDIRection?')
		return Conversions.str_to_scalar_enum(response, enums.DlUlDirection)
