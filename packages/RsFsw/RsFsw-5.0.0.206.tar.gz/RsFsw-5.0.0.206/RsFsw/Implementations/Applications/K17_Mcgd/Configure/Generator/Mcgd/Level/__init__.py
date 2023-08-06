from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 6 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def arLevel(self):
		"""arLevel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_arLevel'):
			from .ArLevel import ArLevel
			self._arLevel = ArLevel(self._core, self._cmd_group)
		return self._arLevel

	@property
	def dutGain(self):
		"""dutGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dutGain'):
			from .DutGain import DutGain
			self._dutGain = DutGain(self._core, self._cmd_group)
		return self._dutGain

	@property
	def dutLimit(self):
		"""dutLimit commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dutLimit'):
			from .DutLimit import DutLimit
			self._dutLimit = DutLimit(self._core, self._cmd_group)
		return self._dutLimit

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.level.set(level = 1.0) \n
		Sets the specified value on the connected signal generator or queries which value is used. \n
			:param level: Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:MCGD:LEVel {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.level.get() \n
		Sets the specified value on the connected signal generator or queries which value is used. \n
			:return: level: Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:LEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
