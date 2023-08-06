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
		"""SCPI: CONFigure[:NR5G]:FELC:STATe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.felc.state.set(state = False) \n
		This command turns the frequency error limit check on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:NR5G:FELC:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure[:NR5G]:FELC:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.felc.state.get() \n
		This command turns the frequency error limit check on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:NR5G:FELC:STATe?')
		return Conversions.str_to_bool(response)
