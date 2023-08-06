from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Active:
	"""Active commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("active", core, parent)

	def set(self, active_count: int) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:COUNt:ACTive \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.count.active.set(active_count = 1) \n
		No command help available \n
			:param active_count: No help available
		"""
		param = Conversions.decimal_value_to_str(active_count)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:COUNt:ACTive {param}')

	def get(self) -> int:
		"""SCPI: CONFigure:WLAN:RUConfig:COUNt:ACTive \n
		Snippet: value: int = driver.applications.k91Wlan.configure.wlan.ruConfig.count.active.get() \n
		No command help available \n
			:return: active_count: No help available"""
		response = self._core.io.query_str(f'CONFigure:WLAN:RUConfig:COUNt:ACTive?')
		return Conversions.str_to_int(response)
