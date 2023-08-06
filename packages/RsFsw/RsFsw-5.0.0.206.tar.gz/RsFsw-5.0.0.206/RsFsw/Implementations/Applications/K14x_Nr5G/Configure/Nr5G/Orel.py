from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Orel:
	"""Orel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("orel", core, parent)

	def set(self, mode: enums.RefPointMode) -> None:
		"""SCPI: CONFigure[:NR5G]:OREL \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.orel.set(mode = enums.RefPointMode.CC1) \n
		This command selects the reference point for frequency offsets of component carriers in a multicarrier setup. \n
			:param mode: CC1 Reference point is the center frequency of first component carrier. GMCFreq Reference point the global multicarrier frequency.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RefPointMode)
		self._core.io.write(f'CONFigure:NR5G:OREL {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.RefPointMode:
		"""SCPI: CONFigure[:NR5G]:OREL \n
		Snippet: value: enums.RefPointMode = driver.applications.k14Xnr5G.configure.nr5G.orel.get() \n
		This command selects the reference point for frequency offsets of component carriers in a multicarrier setup. \n
			:return: mode: No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:OREL?')
		return Conversions.str_to_scalar_enum(response, enums.RefPointMode)
