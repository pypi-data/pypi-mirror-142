from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Highest:
	"""Highest commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("highest", core, parent)

	def get(self) -> int:
		"""SCPI: CONFigure:WLAN:RUConfig:COUNt:HIGHest \n
		Snippet: value: int = driver.applications.k91Wlan.configure.wlan.ruConfig.count.highest.get() \n
		Queries the highest configured RU index in the entire signal. \n
			:return: max_index: Range: 1 to 9"""
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:COUNt:HIGHest?')
		return Conversions.str_to_int(response)
