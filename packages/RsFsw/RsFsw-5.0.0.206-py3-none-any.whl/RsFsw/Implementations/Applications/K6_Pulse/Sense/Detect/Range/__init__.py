from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DETect:RANGe \n
		Snippet: driver.applications.k6Pulse.sense.detect.range.set(state = False) \n
		Enables or disables the use of a detection range instead of the entire capture buffer for analysis. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The entire capture buffer is analyzed. ON | 1 The range defined by [SENSe:]DETect:RANGe:STARt and [SENSe:]DETect:RANGe:LENGth is analyzed.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DETect:RANGe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DETect:RANGe \n
		Snippet: value: bool = driver.applications.k6Pulse.sense.detect.range.get() \n
		Enables or disables the use of a detection range instead of the entire capture buffer for analysis. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The entire capture buffer is analyzed. ON | 1 The range defined by [SENSe:]DETect:RANGe:STARt and [SENSe:]DETect:RANGe:LENGth is analyzed."""
		response = self._core.io.query_str(f'SENSe:DETect:RANGe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Range':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Range(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
