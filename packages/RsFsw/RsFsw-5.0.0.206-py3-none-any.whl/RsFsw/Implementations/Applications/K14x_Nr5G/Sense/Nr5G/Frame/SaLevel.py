from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaLevel:
	"""SaLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saLevel", core, parent)

	def set(self, level: bool) -> None:
		"""SCPI: [SENSe]:NR5G:FRAMe:SALevel \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.frame.saLevel.set(level = False) \n
		This command turns auto leveling for each event in combined measurement sequence on and off. \n
			:param level: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(level)
		self._core.io.write(f'SENSe:NR5G:FRAMe:SALevel {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:NR5G:FRAMe:SALevel \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.nr5G.frame.saLevel.get() \n
		This command turns auto leveling for each event in combined measurement sequence on and off. \n
			:return: level: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:NR5G:FRAMe:SALevel?')
		return Conversions.str_to_bool(response)
