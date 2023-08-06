from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Color:
	"""Color commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("color", core, parent)

	@property
	def style(self):
		"""style commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_style'):
			from .Style import Style
			self._style = Style(self._core, self._cmd_group)
		return self._style

	@property
	def lower(self):
		"""lower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import Lower
			self._lower = Lower(self._core, self._cmd_group)
		return self._lower

	@property
	def upper(self):
		"""upper commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import Upper
			self._upper = Upper(self._core, self._cmd_group)
		return self._upper

	@property
	def shape(self):
		"""shape commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shape'):
			from .Shape import Shape
			self._shape = Shape(self._core, self._cmd_group)
		return self._shape

	@property
	def default(self):
		"""default commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_default'):
			from .Default import Default
			self._default = Default(self._core, self._cmd_group)
		return self._default

	@property
	def truncate(self):
		"""truncate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_truncate'):
			from .Truncate import Truncate
			self._truncate = Truncate(self._core, self._cmd_group)
		return self._truncate

	def clone(self) -> 'Color':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Color(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
