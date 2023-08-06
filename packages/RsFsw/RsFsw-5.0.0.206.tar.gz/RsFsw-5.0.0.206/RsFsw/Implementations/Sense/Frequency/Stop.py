from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:STOP \n
		Snippet: driver.sense.frequency.stop.set(frequency = 1.0) \n
		Defines the stop frequency for a Real-Time measurement. If you set a start frequency that would exceed the maximum span,
		the R&S FSW adjusts the start frequency to stay within the maximum span. \n
			:param frequency: min span to fmax Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:STOP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:STOP \n
		Snippet: value: float = driver.sense.frequency.stop.get() \n
		Defines the stop frequency for a Real-Time measurement. If you set a start frequency that would exceed the maximum span,
		the R&S FSW adjusts the start frequency to stay within the maximum span. \n
			:return: frequency: min span to fmax Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:STOP?')
		return Conversions.str_to_float(response)
