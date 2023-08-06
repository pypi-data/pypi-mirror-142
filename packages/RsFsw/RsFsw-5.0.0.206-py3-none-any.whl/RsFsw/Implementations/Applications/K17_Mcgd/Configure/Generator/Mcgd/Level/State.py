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
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:STATe \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.level.state.set(state = False) \n
		If enabled, the R&S FSW automatically controls the signal level provided by the signal generator as input to the R&S FSW.
		Initially,the value defined by method RsFsw.Applications.K17_Mcgd.Configure.Generator.Mcgd.Level.set is applied.
		Note that the reference level on the R&S FSW is also affected by the signal level. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:MCGD:LEVel:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.configure.generator.mcgd.level.state.get() \n
		If enabled, the R&S FSW automatically controls the signal level provided by the signal generator as input to the R&S FSW.
		Initially,the value defined by method RsFsw.Applications.K17_Mcgd.Configure.Generator.Mcgd.Level.set is applied.
		Note that the reference level on the R&S FSW is also affected by the signal level. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:LEVel:STATe?')
		return Conversions.str_to_bool(response)
