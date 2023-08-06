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
		"""SCPI: CONFigure:REFSignal:CGW:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.refSignal.cgw.ledState.get() \n
		This command queries the processing state of the reference signal generation if the reference signal was designed on a
		signal generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Configure reference signal on a signal generator. \n
			:return: state: GREen Reference signal was successfully generated and loaded into the application. GREY Unknown processing state. RED Reference signal was not successfully generated or loaded into the application."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:CGW:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
