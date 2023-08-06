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
		"""SCPI: [SENSe]:BURSt:COUNt:STATe \n
		Snippet: driver.applications.k9X11Ad.sense.burst.count.state.set(state = False) \n
		If the statistic count is enabled, the specified number of PPDUs is taken into consideration for the statistical
		evaluation (maximally the number of PPDUs detected in the current capture buffer) . If disabled, all detected PPDUs in
		the current capture buffer are considered. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:BURSt:COUNt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:BURSt:COUNt:STATe \n
		Snippet: value: bool = driver.applications.k9X11Ad.sense.burst.count.state.get() \n
		If the statistic count is enabled, the specified number of PPDUs is taken into consideration for the statistical
		evaluation (maximally the number of PPDUs detected in the current capture buffer) . If disabled, all detected PPDUs in
		the current capture buffer are considered. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:BURSt:COUNt:STATe?')
		return Conversions.str_to_bool(response)
