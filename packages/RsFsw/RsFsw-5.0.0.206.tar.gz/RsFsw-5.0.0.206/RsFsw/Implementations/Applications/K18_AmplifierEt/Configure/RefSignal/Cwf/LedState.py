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
		"""SCPI: CONFigure:REFSignal:CWF:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.refSignal.cwf.ledState.get() \n
		This command queries the processing status of a reference signal generated with a waveform file. Available when you
		generate the reference signal with a waveform file. \n
			:return: state: GREen The reference signal was successfully loaded into the application. When method RsFsw.Applications.K18_AmplifierEt.Configure.RefSignal.Cwf.EtGenerator.State.set = ON, this also indicates that the waveform file was accepted by the signal generator. GREY Unknown processing state. RED The reference signal could not have been loaded into the application. When method RsFsw.Applications.K18_AmplifierEt.Configure.RefSignal.Cwf.EtGenerator.State.set = ON, this could also mean that the waveform file was not accepted by the signal generator."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:CWF:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
