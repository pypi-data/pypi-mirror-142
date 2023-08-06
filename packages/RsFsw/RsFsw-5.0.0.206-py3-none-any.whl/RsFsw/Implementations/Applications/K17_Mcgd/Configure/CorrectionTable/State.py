from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, table_state: bool) -> None:
		"""SCPI: CONFigure:CTABle:STATe \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.state.set(table_state = False) \n
		Sets the state of the carrier table. \n
			:param table_state: ON | OFF
		"""
		param = Conversions.bool_to_str(table_state)
		self._core.io.write(f'CONFigure:CTABle:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:CTABle:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.configure.correctionTable.state.get() \n
		Sets the state of the carrier table. \n
			:return: table_state: ON | OFF"""
		response = self._core.io.query_str(f'CONFigure:CTABle:STATe?')
		return Conversions.str_to_bool(response)
