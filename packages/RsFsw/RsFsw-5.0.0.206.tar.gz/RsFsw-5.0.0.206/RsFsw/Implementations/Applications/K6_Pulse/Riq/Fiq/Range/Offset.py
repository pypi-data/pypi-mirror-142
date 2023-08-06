from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: RIQ:FIQ:RANGe:OFFSet \n
		Snippet: driver.applications.k6Pulse.riq.fiq.range.offset.set(time = 1.0) \n
		Defines the starting time of the reference pulse as an offset from the beginning of the data file. \n
			:param time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'RIQ:FIQ:RANGe:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: RIQ:FIQ:RANGe:OFFSet \n
		Snippet: value: float = driver.applications.k6Pulse.riq.fiq.range.offset.get() \n
		Defines the starting time of the reference pulse as an offset from the beginning of the data file. \n
			:return: time: Unit: S"""
		response = self._core.io.query_str(f'RIQ:FIQ:RANGe:OFFSet?')
		return Conversions.str_to_float(response)
