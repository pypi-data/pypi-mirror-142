from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, percentage: float) -> None:
		"""SCPI: [SENSe]:FREQuency:VERify:TOLerance[:RELative] \n
		Snippet: driver.applications.k40PhaseNoise.sense.frequency.verify.tolerance.relative.set(percentage = 1.0) \n
		This command defines a relative frequency tolerance for frequency verification. If you define both an absolute and
		relative tolerance, the application uses the higher tolerance level. \n
			:param percentage: Numeric value in %, relative to the current nominal frequency. Range: 1 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(percentage)
		self._core.io.write(f'SENSe:FREQuency:VERify:TOLerance:RELative {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:VERify:TOLerance[:RELative] \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.frequency.verify.tolerance.relative.get() \n
		This command defines a relative frequency tolerance for frequency verification. If you define both an absolute and
		relative tolerance, the application uses the higher tolerance level. \n
			:return: percentage: Numeric value in %, relative to the current nominal frequency. Range: 1 to 100, Unit: PCT"""
		response = self._core.io.query_str(f'SENSe:FREQuency:VERify:TOLerance:RELative?')
		return Conversions.str_to_float(response)
