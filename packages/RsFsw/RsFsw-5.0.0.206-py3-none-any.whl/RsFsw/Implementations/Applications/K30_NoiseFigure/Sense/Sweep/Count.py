from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, averages: float) -> None:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.count.set(averages = 1.0) \n
		This command defines the number of measurements that are used to average the results. \n
			:param averages: Number of measurements that are performed at a single frequency before average results are displayed. If you set an average of 0 or 1, the application performs a single measurement at each frequency. Range: 0 to 32767
		"""
		param = Conversions.decimal_value_to_str(averages)
		self._core.io.write(f'SENSe:SWEep:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.sweep.count.get() \n
		This command defines the number of measurements that are used to average the results. \n
			:return: averages: Number of measurements that are performed at a single frequency before average results are displayed. If you set an average of 0 or 1, the application performs a single measurement at each frequency. Range: 0 to 32767"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt?')
		return Conversions.str_to_float(response)
