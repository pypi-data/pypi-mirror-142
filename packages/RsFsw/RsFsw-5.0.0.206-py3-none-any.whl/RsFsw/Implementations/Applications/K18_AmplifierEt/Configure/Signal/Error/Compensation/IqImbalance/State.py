from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:SIGNal:ERRor:COMPensation:IQIMbalance[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.signal.error.compensation.iqImbalance.state.set(state = False) \n
		This command turns compensation of the I/Q imbalance on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on estimation of sample rate (method RsFsw.Applications.K18_AmplifierEt.Configure.Signal.Error.Estimation.IqImbalance.State.set) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:SIGNal:ERRor:COMPensation:IQIMbalance:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:SIGNal:ERRor:COMPensation:IQIMbalance[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.signal.error.compensation.iqImbalance.state.get() \n
		This command turns compensation of the I/Q imbalance on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on estimation of sample rate (method RsFsw.Applications.K18_AmplifierEt.Configure.Signal.Error.Estimation.IqImbalance.State.set) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:SIGNal:ERRor:COMPensation:IQIMbalance:STATe?')
		return Conversions.str_to_bool(response)
