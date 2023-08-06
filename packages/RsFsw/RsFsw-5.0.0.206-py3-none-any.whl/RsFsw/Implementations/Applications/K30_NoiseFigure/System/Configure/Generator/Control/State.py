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
		"""SCPI: SYSTem:CONFigure:GENerator:CONTrol:STATe \n
		Snippet: driver.applications.k30NoiseFigure.system.configure.generator.control.state.set(state = False) \n
		This command turns automatic control of an external generator on and off. The command is available with option R&S
		FSW-B10. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:CONFigure:GENerator:CONTrol:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:CONFigure:GENerator:CONTrol:STATe \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.system.configure.generator.control.state.get() \n
		This command turns automatic control of an external generator on and off. The command is available with option R&S
		FSW-B10. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SYSTem:CONFigure:GENerator:CONTrol:STATe?')
		return Conversions.str_to_bool(response)
