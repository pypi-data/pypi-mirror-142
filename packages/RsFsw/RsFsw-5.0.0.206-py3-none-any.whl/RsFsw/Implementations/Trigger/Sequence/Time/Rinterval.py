from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rinterval:
	"""Rinterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rinterval", core, parent)

	def set(self, interval: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:TIME:RINTerval \n
		Snippet: driver.trigger.sequence.time.rinterval.set(interval = 1.0) \n
		This command defines the repetition interval for the time trigger. \n
			:param interval: 2.0 ms to 5000 Range: 2 ns to 5000 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'TRIGger:SEQuence:TIME:RINTerval {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:TIME:RINTerval \n
		Snippet: value: float = driver.trigger.sequence.time.rinterval.get() \n
		This command defines the repetition interval for the time trigger. \n
			:return: interval: 2.0 ms to 5000 Range: 2 ns to 5000 s, Unit: S"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:TIME:RINTerval?')
		return Conversions.str_to_float(response)
