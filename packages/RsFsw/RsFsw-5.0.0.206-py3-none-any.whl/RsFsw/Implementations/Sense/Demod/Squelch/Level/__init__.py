from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import Absolute
			self._absolute = Absolute(self._core, self._cmd_group)
		return self._absolute

	def set(self, threshold: float) -> None:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel \n
		Snippet: driver.sense.demod.squelch.level.set(threshold = 1.0) \n
		This command defines the threshold for selective demodulation. All signals below the threshold are not demodulated. \n
			:param threshold: Percentage of the display height. Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SENSe:DEMod:SQUelch:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel \n
		Snippet: value: float = driver.sense.demod.squelch.level.get() \n
		This command defines the threshold for selective demodulation. All signals below the threshold are not demodulated. \n
			:return: threshold: Percentage of the display height. Range: 0 to 100"""
		response = self._core.io.query_str(f'SENSe:DEMod:SQUelch:LEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
