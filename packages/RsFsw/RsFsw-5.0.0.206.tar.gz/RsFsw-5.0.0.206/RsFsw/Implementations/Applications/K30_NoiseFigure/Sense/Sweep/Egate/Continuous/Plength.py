from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PLENgth \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.continuous.plength.set(time = 1.0) \n
		Defines the length in seconds of a single gate period in continuous gating. The length is determined from the beginning
		of one gate measurement to the beginning of the next one. \n
			:param time: Range: 125 ns to 30 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:SWEep:EGATe:CONTinuous:PLENgth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:CONTinuous:PLENgth \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.sweep.egate.continuous.plength.get() \n
		Defines the length in seconds of a single gate period in continuous gating. The length is determined from the beginning
		of one gate measurement to the beginning of the next one. \n
			:return: time: Range: 125 ns to 30 s, Unit: S"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:CONTinuous:PLENgth?')
		return Conversions.str_to_float(response)
