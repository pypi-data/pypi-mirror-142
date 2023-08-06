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
		"""SCPI: CONFigure:REFSignal:GOS:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.refSignal.gos.ledState.get() \n
		This command queries the processing status of an internally generated reference signal. Available when you configure the
		reference signal within the R&S FSW-K18. \n
			:return: state: GREen Generation of the internally generated reference signal was successful. Transmission of the waveform file to the signal generator was also successful. GREY Unknown transmission state. RED Generation and / or transmission of the internally generated reference signal was not successful."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
