from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class P3Db:
	"""P3Db commands group definition. 10 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("p3Db", core, parent)

	@property
	def inputPy(self):
		"""inputPy commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def out(self):
		"""out commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_out'):
			from .Out import Out
			self._out = Out(self._core, self._cmd_group)
		return self._out

	def clone(self) -> 'P3Db':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = P3Db(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
