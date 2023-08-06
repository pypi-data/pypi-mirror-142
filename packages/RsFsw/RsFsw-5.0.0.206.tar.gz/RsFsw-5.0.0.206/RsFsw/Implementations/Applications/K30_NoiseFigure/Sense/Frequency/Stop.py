from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:STOP \n
		Snippet: driver.applications.k30NoiseFigure.sense.frequency.stop.set(frequency = 1.0) \n
		This command defines the stop frequency. If you change the stop frequency, the application creates a new frequency list. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:STOP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:STOP \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.frequency.stop.get() \n
		This command defines the stop frequency. If you change the stop frequency, the application creates a new frequency list. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:STOP?')
		return Conversions.str_to_float(response)
