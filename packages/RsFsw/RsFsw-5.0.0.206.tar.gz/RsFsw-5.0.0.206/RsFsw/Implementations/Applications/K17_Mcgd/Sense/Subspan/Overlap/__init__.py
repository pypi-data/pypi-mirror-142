from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Overlap:
	"""Overlap commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("overlap", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	def set(self, overlap_frequency: float) -> None:
		"""SCPI: [SENSe]:SUBSpan:OVERlap \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.overlap.set(overlap_frequency = 1.0) \n
		Defines the frequency overlap of subspans for active frequency subspan measurements. \n
			:param overlap_frequency: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(overlap_frequency)
		self._core.io.write(f'SENSe:SUBSpan:OVERlap {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SUBSpan:OVERlap \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.subspan.overlap.get() \n
		Defines the frequency overlap of subspans for active frequency subspan measurements. \n
			:return: overlap_frequency: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:OVERlap?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Overlap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Overlap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
