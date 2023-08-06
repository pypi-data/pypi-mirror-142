from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, average_count: float) -> None:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: driver.sense.average.count.set(average_count = 1.0) \n
		This command defines the number of sweeps that the application uses to average traces. In case of continuous sweep mode,
		the application calculates the moving average over the average count. In case of single sweep mode, the application stops
		the measurement and calculates the average after the average count has been reached. \n
			:param average_count: If you set an average count of 0 or 1, the application performs one single sweep in single sweep mode. In continuous sweep mode, if the average count is set to 0, a moving average over 10 sweeps is performed. Range: 0 to 200000
		"""
		param = Conversions.decimal_value_to_str(average_count)
		self._core.io.write(f'SENSe:AVERage:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: value: float = driver.sense.average.count.get() \n
		This command defines the number of sweeps that the application uses to average traces. In case of continuous sweep mode,
		the application calculates the moving average over the average count. In case of single sweep mode, the application stops
		the measurement and calculates the average after the average count has been reached. \n
			:return: average_count: If you set an average count of 0 or 1, the application performs one single sweep in single sweep mode. In continuous sweep mode, if the average count is set to 0, a moving average over 10 sweeps is performed. Range: 0 to 200000"""
		response = self._core.io.query_str(f'SENSe:AVERage:COUNt?')
		return Conversions.str_to_float(response)
