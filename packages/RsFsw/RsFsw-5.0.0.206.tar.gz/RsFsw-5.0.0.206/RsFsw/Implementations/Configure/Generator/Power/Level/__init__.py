from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:POWer:LEVel \n
		Snippet: driver.configure.generator.power.level.set(level = 1.0) \n
		Defines the output power level used by the connected signal generator. \n
			:param level: numeric value Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:POWer:LEVel {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:POWer:LEVel \n
		Snippet: value: float = driver.configure.generator.power.level.get() \n
		Defines the output power level used by the connected signal generator. \n
			:return: level: numeric value Unit: DBM"""
		response = self._core.io.query_str(f'CONFigure:GENerator:POWer:LEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
