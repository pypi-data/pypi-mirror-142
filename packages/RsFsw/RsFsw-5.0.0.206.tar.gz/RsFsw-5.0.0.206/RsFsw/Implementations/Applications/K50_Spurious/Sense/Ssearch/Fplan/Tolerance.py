from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tolerance:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:SSEarch:FPLan:TOLerance \n
		Snippet: driver.applications.k50Spurious.sense.ssearch.fplan.tolerance.set(frequency = 1.0) \n
		Sets the frequency tolerance to match predicted spurs to measured spurs. \n
			:param frequency: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:SSEarch:FPLan:TOLerance {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SSEarch:FPLan:TOLerance \n
		Snippet: value: float = driver.applications.k50Spurious.sense.ssearch.fplan.tolerance.get() \n
		Sets the frequency tolerance to match predicted spurs to measured spurs. \n
			:return: frequency: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:SSEarch:FPLan:TOLerance?')
		return Conversions.str_to_float(response)
