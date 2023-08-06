from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smode:
	"""Smode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smode", core, parent)

	def set(self, search_mode: enums.SearchMode) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:SMODe \n
		Snippet: driver.sense.adjust.configure.smode.set(search_mode = enums.SearchMode.FAST) \n
		Determines the search mode for the automatic measurement performed to determine the optimal measurement configuration. \n
			:param search_mode: FAST | POPTimzed FAST The measurement is optimized for speed. POPTimzed The measurement is optimized to analyze pulse signals adequately.
		"""
		param = Conversions.enum_scalar_to_str(search_mode, enums.SearchMode)
		self._core.io.write(f'SENSe:ADJust:CONFigure:SMODe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SearchMode:
		"""SCPI: [SENSe]:ADJust:CONFigure:SMODe \n
		Snippet: value: enums.SearchMode = driver.sense.adjust.configure.smode.get() \n
		Determines the search mode for the automatic measurement performed to determine the optimal measurement configuration. \n
			:return: search_mode: FAST | POPTimzed FAST The measurement is optimized for speed. POPTimzed The measurement is optimized to analyze pulse signals adequately."""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.SearchMode)
