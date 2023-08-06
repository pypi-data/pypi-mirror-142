from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:VERify:TOLerance:ABSolute \n
		Snippet: driver.applications.k40PhaseNoise.sense.frequency.verify.tolerance.absolute.set(frequency = 1.0) \n
		This command defines an absolute frequency tolerance for frequency verification. If you define both an absolute and
		relative tolerance, the application uses the higher tolerance level. \n
			:param frequency: Numeric value in Hz. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:VERify:TOLerance:ABSolute {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:VERify:TOLerance:ABSolute \n
		Snippet: value: float = driver.applications.k40PhaseNoise.sense.frequency.verify.tolerance.absolute.get() \n
		This command defines an absolute frequency tolerance for frequency verification. If you define both an absolute and
		relative tolerance, the application uses the higher tolerance level. \n
			:return: frequency: Numeric value in Hz. Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:VERify:TOLerance:ABSolute?')
		return Conversions.str_to_float(response)
