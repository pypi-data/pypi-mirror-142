from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Const:
	"""Const commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("const", core, parent)

	@property
	def ccarrier(self):
		"""ccarrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccarrier'):
			from .Ccarrier import Ccarrier
			self._ccarrier = Ccarrier(self._core, self._cmd_group)
		return self._ccarrier

	@property
	def csymbol(self):
		"""csymbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_csymbol'):
			from .Csymbol import Csymbol
			self._csymbol = Csymbol(self._core, self._cmd_group)
		return self._csymbol

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	def clone(self) -> 'Const':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Const(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
