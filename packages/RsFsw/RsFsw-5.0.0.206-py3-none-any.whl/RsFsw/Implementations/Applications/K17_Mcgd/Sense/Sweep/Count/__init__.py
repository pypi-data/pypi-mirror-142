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
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: driver.applications.k17Mcgd.sense.sweep.count.set(count = 1.0) \n
		This command defines the number of sweep s that the application uses to average traces. During calibration measurements,
		the phase and amplitude values are averaged over the defined number of sweeps. (For Pulse measurements, ) . In continuous
		sweep mode, the application calculates the moving average over the average count. In single sweep mode, the application
		stops the measurement and calculates the average after the average count has been reached. \n
			:param count: If you set a sweep count of 0 or 1, the application performs one single sweep in single sweep mode. In continuous sweep mode, if the average count is set to 0, a moving average over 10 sweeps is performed. Range: 0 to 32767
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:SWEep:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.sweep.count.get() \n
		This command defines the number of sweep s that the application uses to average traces. During calibration measurements,
		the phase and amplitude values are averaged over the defined number of sweeps. (For Pulse measurements, ) . In continuous
		sweep mode, the application calculates the moving average over the average count. In single sweep mode, the application
		stops the measurement and calculates the average after the average count has been reached. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
