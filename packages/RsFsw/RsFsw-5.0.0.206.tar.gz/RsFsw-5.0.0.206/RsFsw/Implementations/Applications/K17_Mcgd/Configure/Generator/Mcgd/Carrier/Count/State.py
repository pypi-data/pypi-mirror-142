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
		"""SCPI: CONFigure:GENerator:MCGD:CARRier:COUNt:STATe \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.carrier.count.state.set(state = False) \n
		If activated, any changes to the number of carriers on the R&S FSW are automatically also applied to the connected signal
		generator. Initially, the value defined by [SENSe:]CARRier:COUNt is applied. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:GENerator:MCGD:CARRier:COUNt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:GENerator:MCGD:CARRier:COUNt:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.configure.generator.mcgd.carrier.count.state.get() \n
		If activated, any changes to the number of carriers on the R&S FSW are automatically also applied to the connected signal
		generator. Initially, the value defined by [SENSe:]CARRier:COUNt is applied. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:CARRier:COUNt:STATe?')
		return Conversions.str_to_bool(response)
