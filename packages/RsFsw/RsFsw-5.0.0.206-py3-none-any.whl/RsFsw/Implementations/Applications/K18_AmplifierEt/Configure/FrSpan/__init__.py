from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrSpan:
	"""FrSpan commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frSpan", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, time: float) -> None:
		"""SCPI: CONFigure:FRSPan \n
		Snippet: driver.applications.k18AmplifierEt.configure.frSpan.set(time = 1.0) \n
		No command help available \n
			:param time: No help available
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:FRSPan {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:FRSPan \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.frSpan.get() \n
		No command help available \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'CONFigure:FRSPan?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'FrSpan':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrSpan(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
