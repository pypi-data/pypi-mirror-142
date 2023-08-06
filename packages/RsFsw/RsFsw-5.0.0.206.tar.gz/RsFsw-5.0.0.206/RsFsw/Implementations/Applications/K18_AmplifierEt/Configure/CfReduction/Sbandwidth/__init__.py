from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sbandwidth:
	"""Sbandwidth commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sbandwidth", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, time: float) -> None:
		"""SCPI: CONFigure:CFReduction:SBANdwidth \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.sbandwidth.set(time = 1.0) \n
		Sets and queries the signal bandwidth. \n
			:param time: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:CFReduction:SBANdwidth {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CFReduction:SBANdwidth \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.cfReduction.sbandwidth.get() \n
		Sets and queries the signal bandwidth. \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:SBANdwidth?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Sbandwidth':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sbandwidth(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
