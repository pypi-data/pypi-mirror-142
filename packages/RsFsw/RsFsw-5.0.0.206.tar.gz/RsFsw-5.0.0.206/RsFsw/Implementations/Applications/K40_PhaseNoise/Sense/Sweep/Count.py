from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, sweep_count: float) -> None:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: driver.applications.k40PhaseNoise.sense.sweep.count.set(sweep_count = 1.0) \n
		This command defines the number of sweeps that the application uses to average traces. (For Pulse measurements, ) .
		In continuous sweep mode, the application calculates the moving average over the average count. In single sweep mode, the
		application stops the measurement and calculates the average after the average count has been reached. \n
			:param sweep_count: If you set a sweep count of 0 or 1, the R&S FSW performs one single sweep. Range: 0 to 200000
		"""
		param = Conversions.decimal_value_to_str(sweep_count)
		self._core.io.write(f'SENSe:SWEep:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.sweep.count.get() \n
		This command defines the number of sweeps that the application uses to average traces. (For Pulse measurements, ) .
		In continuous sweep mode, the application calculates the moving average over the average count. In single sweep mode, the
		application stops the measurement and calculates the average after the average count has been reached. \n
			:return: sweep_count: If you set a sweep count of 0 or 1, the R&S FSW performs one single sweep. Range: 0 to 200000"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt?')
		return Conversions.str_to_float(response)
