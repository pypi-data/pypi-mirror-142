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

	def set(self, direction: enums.DlUlDirection) -> None:
		"""SCPI: CONFigure[:LTE]:LDIRection \n
		Snippet: driver.applications.k10Xlte.configure.lte.ldirection.set(direction = enums.DlUlDirection.DL) \n
		This command selects the link direction. \n
			:param direction: DL Selects the mode to analyze downlink signals. UL Selects the mode to analyze uplink signals.
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.DlUlDirection)
		self._core.io.write(f'CONFigure:LTE:LDIRection {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.DlUlDirection:
		"""SCPI: CONFigure[:LTE]:LDIRection \n
		Snippet: value: enums.DlUlDirection = driver.applications.k10Xlte.configure.lte.ldirection.get() \n
		This command selects the link direction. \n
			:return: direction: DL Selects the mode to analyze downlink signals. UL Selects the mode to analyze uplink signals."""
		response = self._core.io.query_str(f'CONFigure:LTE:LDIRection?')
		return Conversions.str_to_scalar_enum(response, enums.DlUlDirection)
