from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def fhMode(self):
		"""fhMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhMode'):
			from .FhMode import FhMode
			self._fhMode = FhMode(self._core, self._cmd_group)
		return self._fhMode

	@property
	def fhOffset(self):
		"""fhOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhOffset'):
			from .FhOffset import FhOffset
			self._fhOffset = FhOffset(self._core, self._cmd_group)
		return self._fhOffset

	@property
	def fhop(self):
		"""fhop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fhop'):
			from .Fhop import Fhop
			self._fhop = Fhop(self._core, self._cmd_group)
		return self._fhop

	@property
	def nosm(self):
		"""nosm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nosm'):
			from .Nosm import Nosm
			self._nosm = Nosm(self._core, self._cmd_group)
		return self._nosm

	@property
	def plid(self):
		"""plid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plid'):
			from .Plid import Plid
			self._plid = Plid(self._core, self._cmd_group)
		return self._plid

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
