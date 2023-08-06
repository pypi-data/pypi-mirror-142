from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:BURSt:COUNt \n
		Snippet: driver.applications.k9X11Ad.sense.burst.count.set(count = 1.0) \n
		If the statistic count is enabled (see [SENSe:]BURSt:COUNt:STATe) , the specified number of PPDUs is taken into
		consideration for the statistical evaluation (maximally the number of PPDUs detected in the current capture buffer) . If
		disabled, all detected PPDUs in the current capture buffer are considered. \n
			:param count: integer
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:BURSt:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BURSt:COUNt \n
		Snippet: value: float = driver.applications.k9X11Ad.sense.burst.count.get() \n
		If the statistic count is enabled (see [SENSe:]BURSt:COUNt:STATe) , the specified number of PPDUs is taken into
		consideration for the statistical evaluation (maximally the number of PPDUs detected in the current capture buffer) . If
		disabled, all detected PPDUs in the current capture buffer are considered. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:BURSt:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
