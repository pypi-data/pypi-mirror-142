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
		"""SCPI: CONFigure:DPD:AMPM[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.amPm.state.set(state = False) \n
		This command turns AM/PM predistortion on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:DPD:AMPM:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:DPD:AMPM[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.dpd.amPm.state.get() \n
		This command turns AM/PM predistortion on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:DPD:AMPM:STATe?')
		return Conversions.str_to_bool(response)
