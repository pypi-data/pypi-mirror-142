from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Simulation:
	"""Simulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("simulation", core, parent)

	def set(self, simulation: float) -> None:
		"""SCPI: DIAGnostic:SIMulation \n
		Snippet: driver.applications.k149Uwb.diagnostic.simulation.set(simulation = 1.0) \n
		No command help available \n
			:param simulation: No help available
		"""
		param = Conversions.decimal_value_to_str(simulation)
		self._core.io.write(f'DIAGnostic:SIMulation {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SIMulation \n
		Snippet: value: float = driver.applications.k149Uwb.diagnostic.simulation.get() \n
		No command help available \n
			:return: simulation: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SIMulation?')
		return Conversions.str_to_float(response)
