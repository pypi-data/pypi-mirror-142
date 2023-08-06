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
		"""SCPI: CONFigure:GENerator:LEVel:DUTLimit:STATe \n
		Snippet: driver.applications.k14Xnr5G.configure.generator.level.dutLimit.state.set(state = False) \n
		This command turns a limitation of the DUT peak input power on and off. Define the peak input power with method RsFsw.
		Applications.K18_AmplifierEt.Configure.Generator.Level.DutLimit.set.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Level control is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Power.Level.State.set) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:LEVel:DUTLimit:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:LEVel:DUTLimit:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.generator.level.dutLimit.state.get() \n
		This command turns a limitation of the DUT peak input power on and off. Define the peak input power with method RsFsw.
		Applications.K18_AmplifierEt.Configure.Generator.Level.DutLimit.set.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Level control is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Power.Level.State.set) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:GENerator:LEVel:DUTLimit:STATe?')
		return Conversions.str_to_bool(response)
