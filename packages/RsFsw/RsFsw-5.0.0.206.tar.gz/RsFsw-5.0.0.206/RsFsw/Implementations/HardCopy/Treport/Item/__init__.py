from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 13 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	@property
	def default(self):
		"""default commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_default'):
			from .Default import Default
			self._default = Default(self._core, self._cmd_group)
		return self._default

	@property
	def header(self):
		"""header commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_header'):
			from .Header import Header
			self._header = Header(self._core, self._cmd_group)
		return self._header

	@property
	def logo(self):
		"""logo commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_logo'):
			from .Logo import Logo
			self._logo = Logo(self._core, self._cmd_group)
		return self._logo

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def template(self):
		"""template commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_template'):
			from .Template import Template
			self._template = Template(self._core, self._cmd_group)
		return self._template

	def clone(self) -> 'Item':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Item(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
