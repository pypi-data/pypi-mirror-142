from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, gate_length: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:LENGth \n
		Snippet: driver.applications.k30NoiseFigure.sense.sweep.egate.length.set(gate_length = 1.0) \n
		This command defines the gate length. \n
			:param gate_length: Range: 125 ns to 30 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(gate_length)
		self._core.io.write(f'SENSe:SWEep:EGATe:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:LENGth \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.sweep.egate.length.get() \n
		This command defines the gate length. \n
			:return: gate_length: Range: 125 ns to 30 s, Unit: S"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:LENGth?')
		return Conversions.str_to_float(response)
