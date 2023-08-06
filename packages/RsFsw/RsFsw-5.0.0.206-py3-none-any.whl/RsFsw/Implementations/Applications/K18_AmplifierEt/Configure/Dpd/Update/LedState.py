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
		"""SCPI: CONFigure:DPD:UPDate:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.dpd.update.ledState.get() \n
		This command queries the state of the DPD calculation.
			INTRO_CMD_HELP: The information of the return result depends on the DPD method: \n
			- DPD calculated by the generator (with option K541) : Query of the state of the update of the shaping table or the polynomial coefficients.
			- DPD calculation by the Amplifier application: Query of the state of waveform file generation and its upload to the generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:return: state: GREen Transmission was successful. GREY Unknown transmission state. RED Transmission was not successful."""
		response = self._core.io.query_str(f'CONFigure:DPD:UPDate:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
