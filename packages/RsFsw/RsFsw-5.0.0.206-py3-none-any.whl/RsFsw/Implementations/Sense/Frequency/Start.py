from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:STARt \n
		Snippet: driver.sense.frequency.start.set(frequency = 1.0) \n
		Defines the start frequency for a Real-Time measurement. If you set a start frequency that would exceed the maximum span,
		the R&S FSW adjusts the stop frequency to stay within the maximum span. \n
			:param frequency: 0 to (fmax - min span) Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:STARt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:STARt \n
		Snippet: value: float = driver.sense.frequency.start.get() \n
		Defines the start frequency for a Real-Time measurement. If you set a start frequency that would exceed the maximum span,
		the R&S FSW adjusts the stop frequency to stay within the maximum span. \n
			:return: frequency: 0 to (fmax - min span) Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:STARt?')
		return Conversions.str_to_float(response)
