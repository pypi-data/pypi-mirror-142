from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsHelper:
	"""TsHelper commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsHelper", core, parent)

	@property
	def edelay(self):
		"""edelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_edelay'):
			from .Edelay import Edelay
			self._edelay = Edelay(self._core, self._cmd_group)
		return self._edelay

	@property
	def ftrigger(self):
		"""ftrigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftrigger'):
			from .Ftrigger import Ftrigger
			self._ftrigger = Ftrigger(self._core, self._cmd_group)
		return self._ftrigger

	@property
	def rinterval(self):
		"""rinterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rinterval'):
			from .Rinterval import Rinterval
			self._rinterval = Rinterval(self._core, self._cmd_group)
		return self._rinterval

	@property
	def sequence(self):
		"""sequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	def clone(self) -> 'TsHelper':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TsHelper(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
