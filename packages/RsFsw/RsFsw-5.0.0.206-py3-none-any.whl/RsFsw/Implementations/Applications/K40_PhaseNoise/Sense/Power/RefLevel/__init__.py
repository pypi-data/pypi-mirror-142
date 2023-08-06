from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevel:
	"""RefLevel commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	@property
	def verify(self):
		"""verify commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_verify'):
			from .Verify import Verify
			self._verify = Verify(self._core, self._cmd_group)
		return self._verify

	def set(self, power: float) -> None:
		"""SCPI: [SENSe]:POWer:RLEVel \n
		Snippet: driver.applications.k40PhaseNoise.sense.power.refLevel.set(power = 1.0) \n
		This command defines the nominal level. \n
			:param power: Range: -200 to 200, Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SENSe:POWer:RLEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:RLEVel \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.power.refLevel.get() \n
		This command defines the nominal level. \n
			:return: power: Range: -200 to 200, Unit: DBM"""
		response = self._core.io.query_str(f'SENSe:POWer:RLEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'RefLevel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RefLevel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
