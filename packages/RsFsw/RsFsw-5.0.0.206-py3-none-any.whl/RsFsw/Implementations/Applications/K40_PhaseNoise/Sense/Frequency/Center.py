from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer \n
		Snippet: driver.applications.k40PhaseNoise.sense.frequency.center.set(frequency = 1.0) \n
		This command defines the nominal frequency. \n
			:param frequency: Range: 0 to fmax, Unit: HZ fmax is specified in the data sheet. min span is 10 Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:CENTer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.frequency.center.get() \n
		This command defines the nominal frequency. \n
			:return: frequency: Range: 0 to fmax, Unit: HZ fmax is specified in the data sheet. min span is 10 Hz"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer?')
		return Conversions.str_to_float(response)
