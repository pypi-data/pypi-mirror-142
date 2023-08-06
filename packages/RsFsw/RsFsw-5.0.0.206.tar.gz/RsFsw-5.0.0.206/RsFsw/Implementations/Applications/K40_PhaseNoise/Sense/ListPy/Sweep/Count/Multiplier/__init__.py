from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Multiplier:
	"""Multiplier commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiplier", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, multiplier: float) -> None:
		"""SCPI: [SENSe]:LIST:SWEep:COUNt:MULTiplier \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.sweep.count.multiplier.set(multiplier = 1.0) \n
		This command defines a multiplier that is applied to the average count in each half decade. Before you can use the
		command you have to turn on the multiplier with [SENSe:]LIST:SWEep:COUNt:MULTiplier. \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SENSe:LIST:SWEep:COUNt:MULTiplier {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:LIST:SWEep:COUNt:MULTiplier \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.listPy.sweep.count.multiplier.get() \n
		This command defines a multiplier that is applied to the average count in each half decade. Before you can use the
		command you have to turn on the multiplier with [SENSe:]LIST:SWEep:COUNt:MULTiplier. \n
			:return: multiplier: No help available"""
		response = self._core.io.query_str(f'SENSe:LIST:SWEep:COUNt:MULTiplier?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Multiplier':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Multiplier(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
