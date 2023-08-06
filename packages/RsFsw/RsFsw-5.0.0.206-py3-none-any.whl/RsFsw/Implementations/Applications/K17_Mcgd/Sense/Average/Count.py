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
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: driver.applications.k17Mcgd.sense.average.count.set(sweep_count = 1.0) \n
		This command defines the number of sweep s that the application uses to average traces. During calibration measurements,
		the phase and amplitude values are averaged over the defined number of sweeps. In case of continuous sweep mode, the
		application calculates the moving average over the average count. In case of single sweep mode, the application stops the
		measurement and calculates the average after the average count has been reached. \n
			:param sweep_count: No help available
		"""
		param = Conversions.decimal_value_to_str(sweep_count)
		self._core.io.write(f'SENSe:AVERage:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.average.count.get() \n
		This command defines the number of sweep s that the application uses to average traces. During calibration measurements,
		the phase and amplitude values are averaged over the defined number of sweeps. In case of continuous sweep mode, the
		application calculates the moving average over the average count. In case of single sweep mode, the application stops the
		measurement and calculates the average after the average count has been reached. \n
			:return: sweep_count: No help available"""
		response = self._core.io.query_str(f'SENSe:AVERage:COUNt?')
		return Conversions.str_to_float(response)
