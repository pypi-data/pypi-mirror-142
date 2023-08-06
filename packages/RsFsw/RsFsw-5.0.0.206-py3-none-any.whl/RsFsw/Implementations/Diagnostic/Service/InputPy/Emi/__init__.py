from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Emi:
	"""Emi commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emi", core, parent)

	@property
	def spectrum(self):
		"""spectrum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def cfrequency(self):
		"""cfrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfrequency'):
			from .Cfrequency import Cfrequency
			self._cfrequency = Cfrequency(self._core, self._cmd_group)
		return self._cfrequency

	def clone(self) -> 'Emi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Emi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
