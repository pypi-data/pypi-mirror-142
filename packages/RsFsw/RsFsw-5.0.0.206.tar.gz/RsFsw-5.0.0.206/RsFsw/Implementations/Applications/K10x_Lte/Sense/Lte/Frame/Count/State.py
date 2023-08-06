from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe][:LTE]:FRAMe:COUNt:STATe \n
		Snippet: driver.applications.k10Xlte.sense.lte.frame.count.state.set(state = False) \n
		This command turns manual selection of the number of frames you want to analyze on and off. \n
			:param state: ON | 1 You can set the number of frames to analyze. OFF | 0 The R&S FSW analyzes the frames captured in a single sweep.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LTE:FRAMe:COUNt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe][:LTE]:FRAMe:COUNt:STATe \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.lte.frame.count.state.get() \n
		This command turns manual selection of the number of frames you want to analyze on and off. \n
			:return: state: ON | 1 You can set the number of frames to analyze. OFF | 0 The R&S FSW analyzes the frames captured in a single sweep."""
		response = self._core.io.query_str(f'SENSe:LTE:FRAMe:COUNt:STATe?')
		return Conversions.str_to_bool(response)
