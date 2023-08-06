from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:POSTtrigger[:TIME] \n
		Snippet: driver.trigger.sequence.postTrigger.time.set(time = 1.0) \n
		This command defines the length of the posttrigger. \n
			:param time: Length of the posttrigger in seconds. Note that the pre- and posttrigger combined may not be longer than 1 second. Range: 0 s to 1 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:SEQuence:POSTtrigger:TIME {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:POSTtrigger[:TIME] \n
		Snippet: value: float = driver.trigger.sequence.postTrigger.time.get() \n
		This command defines the length of the posttrigger. \n
			:return: time: Length of the posttrigger in seconds. Note that the pre- and posttrigger combined may not be longer than 1 second. Range: 0 s to 1 s, Unit: S"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:POSTtrigger:TIME?')
		return Conversions.str_to_float(response)
