from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:HOLDoff[:TIME] \n
		Snippet: driver.applications.k50Spurious.trigger.sequence.holdoff.time.set(time = 1.0) \n
		Defines the time offset between the trigger event and the start of the measurement. \n
			:param time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:SEQuence:HOLDoff:TIME {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:HOLDoff[:TIME] \n
		Snippet: value: float = driver.applications.k50Spurious.trigger.sequence.holdoff.time.get() \n
		Defines the time offset between the trigger event and the start of the measurement. \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:HOLDoff:TIME?')
		return Conversions.str_to_float(response)
