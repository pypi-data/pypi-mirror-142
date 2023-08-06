from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Temperature:
	"""Temperature commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("temperature", core, parent)

	@property
	def control(self):
		"""control commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	def set(self, temperature: float) -> None:
		"""SCPI: [SENSe]:CORRection:TEMPerature \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.temperature.set(temperature = 1.0) \n
		This command defines the room temperature of the measurement environment. The temperature is taken into account when
		calculating noise results. \n
			:param temperature: Range: 278.15 to 318.15, Unit: K
		"""
		param = Conversions.decimal_value_to_str(temperature)
		self._core.io.write(f'SENSe:CORRection:TEMPerature {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:TEMPerature \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.temperature.get() \n
		This command defines the room temperature of the measurement environment. The temperature is taken into account when
		calculating noise results. \n
			:return: temperature: Range: 278.15 to 318.15, Unit: K"""
		response = self._core.io.query_str(f'SENSe:CORRection:TEMPerature?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Temperature':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Temperature(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
