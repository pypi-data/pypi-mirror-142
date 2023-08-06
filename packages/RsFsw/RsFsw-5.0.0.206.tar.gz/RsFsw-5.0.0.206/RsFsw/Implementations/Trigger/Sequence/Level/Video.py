from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Video:
	"""Video commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("video", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:VIDeo \n
		Snippet: driver.trigger.sequence.level.video.set(level = 1.0) \n
		This command defines the level the video signal must exceed to cause a trigger event. Note that any RF attenuation or
		preamplification is considered when the trigger level is analyzed. \n
			:param level: Range: 0 PCT to 100 PCT, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:VIDeo {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:VIDeo \n
		Snippet: value: float = driver.trigger.sequence.level.video.get() \n
		This command defines the level the video signal must exceed to cause a trigger event. Note that any RF attenuation or
		preamplification is considered when the trigger level is analyzed. \n
			:return: level: Range: 0 PCT to 100 PCT, Unit: PCT"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:VIDeo?')
		return Conversions.str_to_float(response)
