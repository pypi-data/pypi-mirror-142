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
		"""SCPI: CONFigure:GENerator:NPRatio:CONTrol[:STATe] \n
		Snippet: driver.configure.generator.npratio.control.state.set(state = False) \n
		Activates or deactivates control of the signal generator by the R&S FSW. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:CONTrol:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:NPRatio:CONTrol[:STATe] \n
		Snippet: value: bool = driver.configure.generator.npratio.control.state.get() \n
		Activates or deactivates control of the signal generator by the R&S FSW. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:CONTrol:STATe?')
		return Conversions.str_to_bool(response)
