from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, trigger_level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:TDTRigger:LEVel \n
		Snippet: driver.trigger.sequence.tdTrigger.level.set(trigger_level = 1.0) \n
		This command sets the trigger level for the time domain trigger. \n
			:param trigger_level: Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(trigger_level)
		self._core.io.write(f'TRIGger:SEQuence:TDTRigger:LEVel {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:TDTRigger:LEVel \n
		Snippet: value: float = driver.trigger.sequence.tdTrigger.level.get() \n
		This command sets the trigger level for the time domain trigger. \n
			:return: trigger_level: Unit: dBm"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:TDTRigger:LEVel?')
		return Conversions.str_to_float(response)
