from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, assistant_state: bool) -> None:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:STATe \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.state.set(assistant_state = False) \n
		Sets the state of the selected carriers in the configuration assistant. \n
			:param assistant_state: ON | OFF
		"""
		param = Conversions.bool_to_str(assistant_state)
		self._core.io.write(f'CONFigure:CTABle:EDIT:CARRier:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:STATe \n
		Snippet: value: bool = driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.state.get() \n
		Sets the state of the selected carriers in the configuration assistant. \n
			:return: assistant_state: ON | OFF"""
		response = self._core.io.query_str(f'CONFigure:CTABle:EDIT:CARRier:STATe?')
		return Conversions.str_to_bool(response)
