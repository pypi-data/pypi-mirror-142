from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:STARt \n
		Snippet: driver.applications.k40PhaseNoise.sense.frequency.start.set(frequency = 1.0) \n
		This command defines the start frequency of the measurement range. \n
			:param frequency: Offset frequencies in half decade steps. Range: 1 Hz to 100 GHz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:STARt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:STARt \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.frequency.start.get() \n
		This command defines the start frequency of the measurement range. \n
			:return: frequency: Offset frequencies in half decade steps. Range: 1 Hz to 100 GHz, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:STARt?')
		return Conversions.str_to_float(response)
