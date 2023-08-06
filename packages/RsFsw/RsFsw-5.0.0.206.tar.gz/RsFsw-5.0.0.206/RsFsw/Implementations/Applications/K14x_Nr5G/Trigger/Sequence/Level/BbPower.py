from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbPower:
	"""BbPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:BBPower \n
		Snippet: driver.applications.k14Xnr5G.trigger.sequence.level.bbPower.set(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:BBPower {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:BBPower \n
		Snippet: value: float = driver.applications.k14Xnr5G.trigger.sequence.level.bbPower.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:BBPower?')
		return Conversions.str_to_float(response)
