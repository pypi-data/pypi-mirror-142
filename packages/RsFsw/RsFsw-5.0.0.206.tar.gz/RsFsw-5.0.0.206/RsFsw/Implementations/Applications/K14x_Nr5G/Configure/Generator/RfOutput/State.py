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
		"""SCPI: CONFigure:GENerator:RFOutput[:STATe] \n
		Snippet: driver.applications.k14Xnr5G.configure.generator.rfOutput.state.set(state = False) \n
		This command turns the RF output of the generator on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:RFOutput:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:RFOutput[:STATe] \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.generator.rfOutput.state.get() \n
		This command turns the RF output of the generator on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:GENerator:RFOutput:STATe?')
		return Conversions.str_to_bool(response)
