from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def multiplier(self):
		"""multiplier commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiplier'):
			from .Multiplier import Multiplier
			self._multiplier = Multiplier(self._core, self._cmd_group)
		return self._multiplier

	def set(self, averages: float) -> None:
		"""SCPI: [SENSe]:LIST:SWEep:COUNt \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.sweep.count.set(averages = 1.0) \n
		This command defines the number of measurements to be included in the averaging for each and all half decades. \n
			:param averages: Range: 1 to 10000
		"""
		param = Conversions.decimal_value_to_str(averages)
		self._core.io.write(f'SENSe:LIST:SWEep:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:LIST:SWEep:COUNt \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.listPy.sweep.count.get() \n
		This command defines the number of measurements to be included in the averaging for each and all half decades. \n
			:return: averages: Range: 1 to 10000"""
		response = self._core.io.query_str(f'SENSe:LIST:SWEep:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
