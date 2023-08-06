from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfDelta:
	"""CfDelta commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfDelta", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, cf_delta: float) -> None:
		"""SCPI: CONFigure:CFReduction:CFDelta \n
		Snippet: driver.applications.k18AmplifierEt.configure.cfReduction.cfDelta.set(cf_delta = 1.0) \n
		Sets the value difference by which you want to change the crest factor. \n
			:param cf_delta: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(cf_delta)
		self._core.io.write(f'CONFigure:CFReduction:CFDelta {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:CFReduction:CFDelta \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.cfReduction.cfDelta.get() \n
		Sets the value difference by which you want to change the crest factor. \n
			:return: cf_delta: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:CFDelta?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'CfDelta':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CfDelta(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
