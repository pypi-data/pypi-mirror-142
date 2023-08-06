from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Joined:
	"""Joined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("joined", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:WLAN:RSYNc:JOINed \n
		Snippet: driver.applications.k91Wlan.configure.wlan.rsync.joined.set(state = False) \n
		This command configures how PPDU synchronization and tracking is performed for multiple antennas. \n
			:param state: ON | OFF | 1 | 0 ON | 1 RX antennas are synchronized and tracked together. OFF | 0 RX antennas are synchronized and tracked separately.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:WLAN:RSYNc:JOINed {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:WLAN:RSYNc:JOINed \n
		Snippet: value: bool = driver.applications.k91Wlan.configure.wlan.rsync.joined.get() \n
		This command configures how PPDU synchronization and tracking is performed for multiple antennas. \n
			:return: state: ON | OFF | 1 | 0 ON | 1 RX antennas are synchronized and tracked together. OFF | 0 RX antennas are synchronized and tracked separately."""
		response = self._core.io.query_str(f'CONFigure:WLAN:RSYNc:JOINed?')
		return Conversions.str_to_bool(response)
