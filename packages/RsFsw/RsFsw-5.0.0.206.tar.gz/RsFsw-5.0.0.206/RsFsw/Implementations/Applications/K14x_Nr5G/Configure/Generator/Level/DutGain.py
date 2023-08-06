from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DutGain:
	"""DutGain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dutGain", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:LEVel:DUTGain \n
		Snippet: driver.applications.k14Xnr5G.configure.generator.level.dutGain.set(level = 1.0) \n
		This command defines DUT level gain for generator level control.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Level control is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Power.Level.State.set) . \n
			:param level: Unit: dB
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:LEVel:DUTGain {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:LEVel:DUTGain \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.generator.level.dutGain.get() \n
		This command defines DUT level gain for generator level control.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) .
			- Level control is on (method RsFsw.Applications.K14x_Nr5G.Configure.Generator.Power.Level.State.set) . \n
			:return: level: Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:GENerator:LEVel:DUTGain?')
		return Conversions.str_to_float(response)
