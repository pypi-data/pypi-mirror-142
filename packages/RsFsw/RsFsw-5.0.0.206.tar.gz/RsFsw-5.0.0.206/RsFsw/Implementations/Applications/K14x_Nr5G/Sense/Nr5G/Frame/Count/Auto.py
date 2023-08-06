from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:COUNt:AUTO \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.count.auto.set(state = False) \n
		This command turns automatic selection of the number of frames to analyze on and off. \n
			:param state: ON | 1 Selects the analyzed number of frames as specified by 3GPP. OFF | 0 Turns on manual selection of the number of frames.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:NR5G:FRAMe:COUNt:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:FRAMe:COUNt:AUTO \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.frame.count.auto.get() \n
		This command turns automatic selection of the number of frames to analyze on and off. \n
			:return: state: ON | 1 Selects the analyzed number of frames as specified by 3GPP. OFF | 0 Turns on manual selection of the number of frames."""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:COUNt:AUTO?')
		return Conversions.str_to_bool(response)
