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
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:ARLevel[:STATe] \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.level.arLevel.state.set(state = False) \n
		Determines the behavior of the reference level. \n
			:param state: ON | OFF | 0 | 1 ON | 1 The R&S FSW automatically adapts the reference level if 'Level (RMS) ' or the 'DUT Gain' is changed. OFF | 0 The reference level is not automatically adapted.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:MCGD:LEVel:ARLevel:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:ARLevel[:STATe] \n
		Snippet: value: bool = driver.applications.k17Mcgd.configure.generator.mcgd.level.arLevel.state.get() \n
		Determines the behavior of the reference level. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 The R&S FSW automatically adapts the reference level if 'Level (RMS) ' or the 'DUT Gain' is changed. OFF | 0 The reference level is not automatically adapted."""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:LEVel:ARLevel:STATe?')
		return Conversions.str_to_bool(response)
