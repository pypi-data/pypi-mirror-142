from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Points:
	"""Points commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("points", core, parent)

	def set(self, sweep_points: int) -> None:
		"""SCPI: [SENSe]:SWEep:POINts \n
		Snippet: driver.sense.sweep.points.set(sweep_points = 1) \n
		No command help available \n
			:param sweep_points: No help available
		"""
		param = Conversions.decimal_value_to_str(sweep_points)
		self._core.io.write(f'SENSe:SWEep:POINts {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:SWEep:POINts \n
		Snippet: value: int = driver.sense.sweep.points.get() \n
		No command help available \n
			:return: sweep_points: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:POINts?')
		return Conversions.str_to_int(response)
