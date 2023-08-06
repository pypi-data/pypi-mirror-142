from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tolerance:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, tol: float) -> None:
		"""SCPI: [SENSe]:CREFerence:HARMonics:TOLerance \n
		Snippet: driver.applications.k50Spurious.sense.creference.harmonics.tolerance.set(tol = 1.0) \n
		Sets the frequency tolerance to match harmonics to measured spurs. \n
			:param tol: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(tol)
		self._core.io.write(f'SENSe:CREFerence:HARMonics:TOLerance {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CREFerence:HARMonics:TOLerance \n
		Snippet: value: float = driver.applications.k50Spurious.sense.creference.harmonics.tolerance.get() \n
		Sets the frequency tolerance to match harmonics to measured spurs. \n
			:return: tol: No help available"""
		response = self._core.io.query_str(f'SENSe:CREFerence:HARMonics:TOLerance?')
		return Conversions.str_to_float(response)
