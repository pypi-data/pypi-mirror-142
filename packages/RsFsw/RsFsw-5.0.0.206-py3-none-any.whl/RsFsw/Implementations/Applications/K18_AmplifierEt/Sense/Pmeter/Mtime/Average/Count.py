from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, number_readings: float) -> None:
		"""SCPI: [SENSe]:PMETer:MTIMe:AVERage:COUNt \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.mtime.average.count.set(number_readings = 1.0) \n
		This command sets the number of power readings included in the averaging process of power sensor measurements. Extended
		averaging yields more stable results for power sensor measurements, especially for measurements on signals with a low
		power, because it minimizes the effects of noise. \n
			:param number_readings: An average count of 0 or 1 performs one power reading. Range: 0 to 256
		"""
		param = Conversions.decimal_value_to_str(number_readings)
		self._core.io.write(f'SENSe:PMETer:MTIMe:AVERage:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:MTIMe:AVERage:COUNt \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.mtime.average.count.get() \n
		This command sets the number of power readings included in the averaging process of power sensor measurements. Extended
		averaging yields more stable results for power sensor measurements, especially for measurements on signals with a low
		power, because it minimizes the effects of noise. \n
			:return: number_readings: An average count of 0 or 1 performs one power reading. Range: 0 to 256"""
		response = self._core.io.query_str(f'SENSe:PMETer:MTIMe:AVERage:COUNt?')
		return Conversions.str_to_float(response)
