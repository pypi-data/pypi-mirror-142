from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:EQUalizer[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.equalizer.state.set(state = False) \n
		This command turns the equalizer on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Load equalizer filter data (either by training or by restoring a file with equalizer information) .
			Table Header:  \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Equalizer.Train.set
			- method RsFsw.Applications.K18_AmplifierEt.MassMemory.Load.Equalizer.FilterPy.Coefficient.set \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:EQUalizer:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:EQUalizer[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.equalizer.state.get() \n
		This command turns the equalizer on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Load equalizer filter data (either by training or by restoring a file with equalizer information) .
			Table Header:  \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Equalizer.Train.set
			- method RsFsw.Applications.K18_AmplifierEt.MassMemory.Load.Equalizer.FilterPy.Coefficient.set \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:EQUalizer:STATe?')
		return Conversions.str_to_bool(response)
