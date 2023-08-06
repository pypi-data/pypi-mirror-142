from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 5 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	@property
	def step(self):
		"""step commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer \n
		Snippet: driver.sense.frequency.center.set(frequency = 1.0) \n
		This command defines the center frequency. \n
			:param frequency: The allowed range and fmax is specified in the data sheet. UP Increases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. DOWN Decreases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:CENTer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer \n
		Snippet: value: float = driver.sense.frequency.center.get() \n
		This command defines the center frequency. \n
			:return: frequency: The allowed range and fmax is specified in the data sheet. UP Increases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. DOWN Decreases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Center':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Center(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
