from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:DDPD:APPLy[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.apply.state.set(state = False) \n
		This command transfers the waveform file with the correction values to the signal generator and applies them to the input
		signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Run a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:DDPD:APPLy:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:DDPD:APPLy[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.ddpd.apply.state.get() \n
		This command transfers the waveform file with the correction values to the signal generator and applies them to the input
		signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Run a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:DDPD:APPLy:STATe?')
		return Conversions.str_to_bool(response)
