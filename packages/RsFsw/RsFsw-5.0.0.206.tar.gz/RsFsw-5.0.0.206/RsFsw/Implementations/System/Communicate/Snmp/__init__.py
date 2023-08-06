from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snmp:
	"""Snmp commands group definition. 9 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snmp", core, parent)

	@property
	def community(self):
		"""community commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_community'):
			from .Community import Community
			self._community = Community(self._core, self._cmd_group)
		return self._community

	@property
	def version(self):
		"""version commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_version'):
			from .Version import Version
			self._version = Version(self._core, self._cmd_group)
		return self._version

	@property
	def location(self):
		"""location commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_location'):
			from .Location import Location
			self._location = Location(self._core, self._cmd_group)
		return self._location

	@property
	def contact(self):
		"""contact commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_contact'):
			from .Contact import Contact
			self._contact = Contact(self._core, self._cmd_group)
		return self._contact

	@property
	def usm(self):
		"""usm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usm'):
			from .Usm import Usm
			self._usm = Usm(self._core, self._cmd_group)
		return self._usm

	def clone(self) -> 'Snmp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Snmp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
