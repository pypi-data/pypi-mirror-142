from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:REFSignal:CWF:ETGenerator[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cwf.etGenerator.state.set(state = False) \n
		This command turns the transfer of the reference signal data to a generator on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Generate reference signal with a waveform file \n
			:param state: ON | 1 Reference signal data is transferred to the generator and generated with the generator. OFF | 0 Reference signal data is loaded into the application without transferring the waveform to the generator. When you turn it off, you have to define the peak input power of the DUT with method RsFsw.Applications.K18_AmplifierEt.Configure.RefSignal.Cwf.DpiPower.set. Otherwise, measurement result may be invalid.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:REFSignal:CWF:ETGenerator:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:REFSignal:CWF:ETGenerator[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.refSignal.cwf.etGenerator.state.get() \n
		This command turns the transfer of the reference signal data to a generator on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Generate reference signal with a waveform file \n
			:return: state: ON | 1 Reference signal data is transferred to the generator and generated with the generator. OFF | 0 Reference signal data is loaded into the application without transferring the waveform to the generator. When you turn it off, you have to define the peak input power of the DUT with method RsFsw.Applications.K18_AmplifierEt.Configure.RefSignal.Cwf.DpiPower.set. Otherwise, measurement result may be invalid."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:CWF:ETGenerator:STATe?')
		return Conversions.str_to_bool(response)
