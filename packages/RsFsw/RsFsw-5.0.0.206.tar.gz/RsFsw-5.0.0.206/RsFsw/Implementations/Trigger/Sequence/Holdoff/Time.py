from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, offset: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:HOLDoff[:TIME] \n
		Snippet: driver.trigger.sequence.holdoff.time.set(offset = 1.0) \n
		Defines the time offset between the trigger event and the start of the sweep. \n
			:param offset: For measurements in the frequency domain, the range is 0 s to 30 s. For measurements in the time domain, the range is the negative sweep time to 30 s. Unit: S
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'TRIGger:SEQuence:HOLDoff:TIME {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:HOLDoff[:TIME] \n
		Snippet: value: float = driver.trigger.sequence.holdoff.time.get() \n
		Defines the time offset between the trigger event and the start of the sweep. \n
			:return: offset: For measurements in the frequency domain, the range is 0 s to 30 s. For measurements in the time domain, the range is the negative sweep time to 30 s. Unit: S"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:HOLDoff:TIME?')
		return Conversions.str_to_float(response)
