from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Treport:
	"""Treport commands group definition. 29 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("treport", core, parent)

	@property
	def append(self):
		"""append commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_append'):
			from .Append import Append
			self._append = Append(self._core, self._cmd_group)
		return self._append

	@property
	def description(self):
		"""description commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_description'):
			from .Description import Description
			self._description = Description(self._core, self._cmd_group)
		return self._description

	@property
	def item(self):
		"""item commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_item'):
			from .Item import Item
			self._item = Item(self._core, self._cmd_group)
		return self._item

	@property
	def new(self):
		"""new commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_new'):
			from .New import New
			self._new = New(self._core, self._cmd_group)
		return self._new

	@property
	def pageSize(self):
		"""pageSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pageSize'):
			from .PageSize import PageSize
			self._pageSize = PageSize(self._core, self._cmd_group)
		return self._pageSize

	@property
	def pcolors(self):
		"""pcolors commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcolors'):
			from .Pcolors import Pcolors
			self._pcolors = Pcolors(self._core, self._cmd_group)
		return self._pcolors

	@property
	def pagecount(self):
		"""pagecount commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pagecount'):
			from .Pagecount import Pagecount
			self._pagecount = Pagecount(self._core, self._cmd_group)
		return self._pagecount

	@property
	def tdDtamp(self):
		"""tdDtamp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdDtamp'):
			from .TdDtamp import TdDtamp
			self._tdDtamp = TdDtamp(self._core, self._cmd_group)
		return self._tdDtamp

	@property
	def test(self):
		"""test commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_test'):
			from .Test import Test
			self._test = Test(self._core, self._cmd_group)
		return self._test

	@property
	def title(self):
		"""title commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_title'):
			from .Title import Title
			self._title = Title(self._core, self._cmd_group)
		return self._title

	def clone(self) -> 'Treport':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Treport(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
