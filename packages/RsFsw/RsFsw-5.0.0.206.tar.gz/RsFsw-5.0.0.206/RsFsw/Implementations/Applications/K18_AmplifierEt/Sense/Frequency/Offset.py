from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:OFFSet \n
		Snippet: driver.applications.k18AmplifierEt.sense.frequency.offset.set(frequency = 1.0) \n
		This command defines a frequency offset. If this value is not 0 Hz, the application assumes that the input signal was
		frequency shifted outside the application. All results of type 'frequency' will be corrected for this shift numerically
		by the application. \n
			:param frequency: Range: -1 THz to 1 THz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:OFFSet \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.frequency.offset.get() \n
		This command defines a frequency offset. If this value is not 0 Hz, the application assumes that the input signal was
		frequency shifted outside the application. All results of type 'frequency' will be corrected for this shift numerically
		by the application. \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)
