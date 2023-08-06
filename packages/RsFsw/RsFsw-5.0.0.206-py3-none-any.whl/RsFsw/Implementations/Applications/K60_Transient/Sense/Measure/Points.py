from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Points:
	"""Points commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("points", core, parent)

	def set(self, measurement_points: float) -> None:
		"""SCPI: [SENSe]:MEASure:POINts \n
		Snippet: driver.applications.k60Transient.sense.measure.points.set(measurement_points = 1.0) \n
		No command help available \n
			:param measurement_points: No help available
		"""
		param = Conversions.decimal_value_to_str(measurement_points)
		self._core.io.write(f'SENSe:MEASure:POINts {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MEASure:POINts \n
		Snippet: value: float = driver.applications.k60Transient.sense.measure.points.get() \n
		No command help available \n
			:return: measurement_points: No help available"""
		response = self._core.io.query_str(f'SENSe:MEASure:POINts?')
		return Conversions.str_to_float(response)
