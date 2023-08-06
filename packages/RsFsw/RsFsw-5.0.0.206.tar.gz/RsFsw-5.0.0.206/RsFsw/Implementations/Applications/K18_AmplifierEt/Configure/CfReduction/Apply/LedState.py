from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedState:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.LedState:
		"""SCPI: CONFigure:CFReduction:APPLy:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.cfReduction.apply.ledState.get() \n
		Reads the LED status of crest factor reduction apply on the connected signal generator. Only available for backward
		compatibility, use method RsFsw.Applications.K18_AmplifierEt.Configure.CfReduction.Read.LedState.get_ instead. \n
			:return: state: GREY | RED | GREen"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:APPLy:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
