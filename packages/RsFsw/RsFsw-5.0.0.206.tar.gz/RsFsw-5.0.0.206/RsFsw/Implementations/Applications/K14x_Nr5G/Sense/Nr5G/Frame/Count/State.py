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
		"""SCPI: [SENSe]:NR5G:FRAMe:COUNt:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.count.state.set(state = False) \n
		This command turns manual definition of number of frames to analyze on and off. \n
			:param state: OFF | 0 The R&S FSW analyzes all frames in the capture buffer. ON | 1 Define the number of frames to analyze with [SENSe:]NR5G:FRAMe:COUNt.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:FRAMe:COUNt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:FRAMe:COUNt:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.frame.count.state.get() \n
		This command turns manual definition of number of frames to analyze on and off. \n
			:return: state: OFF | 0 The R&S FSW analyzes all frames in the capture buffer. ON | 1 Define the number of frames to analyze with [SENSe:]NR5G:FRAMe:COUNt."""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:COUNt:STATe?')
		return Conversions.str_to_bool(response)
