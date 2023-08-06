from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class High:
	"""High commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, freq_high: float) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH \n
		Snippet: driver.sense.mixer.harmonic.high.set(freq_high = 1.0) \n
		No command help available \n
			:param freq_high: No help available
		"""
		param = Conversions.decimal_value_to_str(freq_high)
		self._core.io.write(f'SENSe:MIXer:HARMonic:HIGH {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:HARMonic:HIGH \n
		Snippet: value: float = driver.sense.mixer.harmonic.high.get() \n
		No command help available \n
			:return: freq_high: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:HIGH?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'High':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = High(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
