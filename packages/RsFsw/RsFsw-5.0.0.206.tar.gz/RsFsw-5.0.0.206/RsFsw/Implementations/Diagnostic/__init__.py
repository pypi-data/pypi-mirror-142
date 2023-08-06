from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Diagnostic:
	"""Diagnostic commands group definition. 55 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagnostic", core, parent)

	@property
	def hums(self):
		"""hums commands group. 13 Sub-classes, 2 commands."""
		if not hasattr(self, '_hums'):
			from .Hums import Hums
			self._hums = Hums(self._core, self._cmd_group)
		return self._hums

	@property
	def service(self):
		"""service commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_service'):
			from .Service import Service
			self._service = Service(self._core, self._cmd_group)
		return self._service

	@property
	def info(self):
		"""info commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	def clone(self) -> 'Diagnostic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Diagnostic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
