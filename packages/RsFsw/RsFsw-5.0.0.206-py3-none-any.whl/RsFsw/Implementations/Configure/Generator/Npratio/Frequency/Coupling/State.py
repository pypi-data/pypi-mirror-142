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
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency:COUPling[:STATe] \n
		Snippet: driver.configure.generator.npratio.frequency.coupling.state.set(state = False) \n
		Enables or disables frequency coupling between the R&S FSW and the connected generator. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off A fixed frequency is used by the generator. ON | 1 Switches the function on The frequency defined on the analyzer is automatically also used by the generator.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:FREQuency:COUPling:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency:COUPling[:STATe] \n
		Snippet: value: bool = driver.configure.generator.npratio.frequency.coupling.state.get() \n
		Enables or disables frequency coupling between the R&S FSW and the connected generator. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off A fixed frequency is used by the generator. ON | 1 Switches the function on The frequency defined on the analyzer is automatically also used by the generator."""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:FREQuency:COUPling:STATe?')
		return Conversions.str_to_bool(response)
