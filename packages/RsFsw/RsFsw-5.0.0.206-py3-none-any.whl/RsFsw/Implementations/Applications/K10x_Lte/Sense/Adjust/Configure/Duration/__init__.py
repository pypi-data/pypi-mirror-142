from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, duration: float) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:DURation \n
		Snippet: driver.applications.k10Xlte.sense.adjust.configure.duration.set(duration = 1.0) \n
		No command help available \n
			:param duration: No help available
		"""
		param = Conversions.decimal_value_to_str(duration)
		self._core.io.write(f'SENSe:ADJust:CONFigure:DURation {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:CONFigure:DURation \n
		Snippet: value: float = driver.applications.k10Xlte.sense.adjust.configure.duration.get() \n
		No command help available \n
			:return: duration: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:DURation?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Duration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Duration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
