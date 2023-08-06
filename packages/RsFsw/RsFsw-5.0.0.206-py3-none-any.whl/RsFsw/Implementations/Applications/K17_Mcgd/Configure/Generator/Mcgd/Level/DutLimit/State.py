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
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:DUTLimit:STATe \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.level.dutLimit.state.set(state = False) \n
		If activated, the generator does not exceed the maximum input power (peak envelope power, 'PEP') that is currently
		allowed by the DUT. To query or define the current PEP limit value, use method RsFsw.Applications.K17_Mcgd.Configure.
		Generator.Mcgd.Level.DutLimit.set. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:MCGD:LEVel:DUTLimit:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:DUTLimit:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.configure.generator.mcgd.level.dutLimit.state.get() \n
		If activated, the generator does not exceed the maximum input power (peak envelope power, 'PEP') that is currently
		allowed by the DUT. To query or define the current PEP limit value, use method RsFsw.Applications.K17_Mcgd.Configure.
		Generator.Mcgd.Level.DutLimit.set. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:LEVel:DUTLimit:STATe?')
		return Conversions.str_to_bool(response)
