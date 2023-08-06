from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fm:
	"""Fm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fm", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:FM \n
		Snippet: driver.trigger.sequence.level.fm.set(level = 1.0) \n
		The command sets the level when FM-modulated signals are used as trigger source. For triggering to be successful, the
		measurement time must cover at least 5 periods of the audio signal. \n
			:param level: Range: -10 to +10, Unit: MHz
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:FM {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:FM \n
		Snippet: value: float = driver.trigger.sequence.level.fm.get() \n
		The command sets the level when FM-modulated signals are used as trigger source. For triggering to be successful, the
		measurement time must cover at least 5 periods of the audio signal. \n
			:return: level: Range: -10 to +10, Unit: MHz"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:FM?')
		return Conversions.str_to_float(response)
