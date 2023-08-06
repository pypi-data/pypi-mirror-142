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
		"""SCPI: CONFigure:DPD:AMPM:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.dpd.amPm.ledState.get() \n
		This command queries the state of the calculation of the AM/PM distortion curve. \n
			:return: state: GREen Calculation was successful. GREY Unknown calculation state. RED Calculation was not successful."""
		response = self._core.io.query_str(f'CONFigure:DPD:AMPM:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
