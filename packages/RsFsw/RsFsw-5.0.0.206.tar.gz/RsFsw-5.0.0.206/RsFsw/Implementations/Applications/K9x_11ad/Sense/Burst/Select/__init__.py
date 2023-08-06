from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, count: int) -> None:
		"""SCPI: [SENSe]:BURSt:SELect \n
		Snippet: driver.applications.k9X11Ad.sense.burst.select.set(count = 1) \n
		If single PPDU analysis is enabled (see [SENSe:]BURSt:SELect:STATe) , the IEEE 802.11ad I/Q results are based on the
		specified PPDU. If disabled, all detected PPDUs in the current capture buffer are evaluated. \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:BURSt:SELect {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:BURSt:SELect \n
		Snippet: value: int = driver.applications.k9X11Ad.sense.burst.select.get() \n
		If single PPDU analysis is enabled (see [SENSe:]BURSt:SELect:STATe) , the IEEE 802.11ad I/Q results are based on the
		specified PPDU. If disabled, all detected PPDUs in the current capture buffer are evaluated. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:BURSt:SELect?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Select':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Select(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
