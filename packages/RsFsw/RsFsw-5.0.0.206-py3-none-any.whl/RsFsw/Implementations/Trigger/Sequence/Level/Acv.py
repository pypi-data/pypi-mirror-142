from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acv:
	"""Acv commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acv", core, parent)

	def set(self, trigger_level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:ACV \n
		Snippet: driver.trigger.sequence.level.acv.set(trigger_level = 1.0) \n
		No command help available \n
			:param trigger_level: No help available
		"""
		param = Conversions.decimal_value_to_str(trigger_level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:ACV {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:ACV \n
		Snippet: value: float = driver.trigger.sequence.level.acv.get() \n
		No command help available \n
			:return: trigger_level: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:ACV?')
		return Conversions.str_to_float(response)
