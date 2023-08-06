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
		"""SCPI: DISPlay[:WINDow]:MINFo[:STATe] \n
		Snippet: driver.applications.k149Uwb.display.window.minfo.state.set(state = False) \n
		This command turns the marker information in all diagrams on and off. \n
			:param state: ON | 1 Displays the marker information in the diagrams. OFF | 0 Hides the marker information in the diagrams.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:WINDow:MINFo:STATe {param}')

	def get(self) -> bool:
		"""SCPI: DISPlay[:WINDow]:MINFo[:STATe] \n
		Snippet: value: bool = driver.applications.k149Uwb.display.window.minfo.state.get() \n
		This command turns the marker information in all diagrams on and off. \n
			:return: state: ON | 1 Displays the marker information in the diagrams. OFF | 0 Hides the marker information in the diagrams."""
		response = self._core.io.query_str(f'DISPlay:WINDow:MINFo:STATe?')
		return Conversions.str_to_bool(response)
