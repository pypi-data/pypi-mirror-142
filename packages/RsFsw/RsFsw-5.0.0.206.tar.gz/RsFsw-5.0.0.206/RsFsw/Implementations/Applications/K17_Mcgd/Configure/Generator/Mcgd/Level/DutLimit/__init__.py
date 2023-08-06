from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DutLimit:
	"""DutLimit commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dutLimit", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:DUTLimit \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.level.dutLimit.set(level = 1.0) \n
		Sets or queries the maximum input power (peak envelope power, 'PEP') that is currently allowed by the DUT and that is
		specified on the generator. The generator output does not exceed this value. \n
			:param level: Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:MCGD:LEVel:DUTLimit {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:LEVel:DUTLimit \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.level.dutLimit.get() \n
		Sets or queries the maximum input power (peak envelope power, 'PEP') that is currently allowed by the DUT and that is
		specified on the generator. The generator output does not exceed this value. \n
			:return: level: Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:LEVel:DUTLimit?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DutLimit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DutLimit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
