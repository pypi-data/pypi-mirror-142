from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FhFrame:
	"""FhFrame commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhFrame", core, parent)

	@property
	def real(self):
		"""real commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_real'):
			from .Real import Real
			self._real = Real(self._core, self._cmd_group)
		return self._real

	@property
	def imaginary(self):
		"""imaginary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imaginary'):
			from .Imaginary import Imaginary
			self._imaginary = Imaginary(self._core, self._cmd_group)
		return self._imaginary

	def clone(self) -> 'FhFrame':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FhFrame(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
