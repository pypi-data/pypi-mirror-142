from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Points:
	"""Points commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("points", core, parent)

	def set(self, sweep_points: float) -> None:
		"""SCPI: [SENSe]:FREQuency:POINts \n
		Snippet: driver.applications.k30NoiseFigure.sense.frequency.points.set(sweep_points = 1.0) \n
		This command defines the number of measurement points analyzed during a sweep. \n
			:param sweep_points: Range: 1 to 10001
		"""
		param = Conversions.decimal_value_to_str(sweep_points)
		self._core.io.write(f'SENSe:FREQuency:POINts {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:POINts \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.frequency.points.get() \n
		This command defines the number of measurement points analyzed during a sweep. \n
			:return: sweep_points: Range: 1 to 10001"""
		response = self._core.io.query_str(f'SENSe:FREQuency:POINts?')
		return Conversions.str_to_float(response)
