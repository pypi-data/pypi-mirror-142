from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: RIQ:FIQ:RANGe:LENGth \n
		Snippet: driver.applications.k6Pulse.riq.fiq.range.length.set(time = 1.0) \n
		Defines the length of the reference pulse in the data file in seconds. \n
			:param time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'RIQ:FIQ:RANGe:LENGth {param}')

	def get(self) -> float:
		"""SCPI: RIQ:FIQ:RANGe:LENGth \n
		Snippet: value: float = driver.applications.k6Pulse.riq.fiq.range.length.get() \n
		Defines the length of the reference pulse in the data file in seconds. \n
			:return: time: Unit: S"""
		response = self._core.io.query_str(f'RIQ:FIQ:RANGe:LENGth?')
		return Conversions.str_to_float(response)
