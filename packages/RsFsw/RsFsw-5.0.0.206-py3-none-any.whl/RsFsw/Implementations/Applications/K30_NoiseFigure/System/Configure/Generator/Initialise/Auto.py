from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:CONFigure:GENerator:INITialise:AUTO \n
		Snippet: driver.applications.k30NoiseFigure.system.configure.generator.initialise.auto.set(state = False) \n
		This command turns automatic connection to the generator on and off. If on, the application automatically configures the
		generator before each measurement and turns on its RF output. Note that you have to establish a connection to the
		generator before you can perform the measurement. The command is available with option R&S FSW-B10. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:CONFigure:GENerator:INITialise:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:CONFigure:GENerator:INITialise:AUTO \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.system.configure.generator.initialise.auto.get() \n
		This command turns automatic connection to the generator on and off. If on, the application automatically configures the
		generator before each measurement and turns on its RF output. Note that you have to establish a connection to the
		generator before you can perform the measurement. The command is available with option R&S FSW-B10. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SYSTem:CONFigure:GENerator:INITialise:AUTO?')
		return Conversions.str_to_bool(response)
