from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fpeaks:
	"""Fpeaks commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fpeaks", core, parent)

	@property
	def annotation(self):
		"""annotation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_annotation'):
			from .Annotation import Annotation
			self._annotation = Annotation(self._core, self._cmd_group)
		return self._annotation

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import Immediate
			self._immediate = Immediate(self._core, self._cmd_group)
		return self._immediate

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def search(self):
		"""search commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_search'):
			from .Search import Search
			self._search = Search(self._core, self._cmd_group)
		return self._search

	@property
	def sort(self):
		"""sort commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sort'):
			from .Sort import Sort
			self._sort = Sort(self._core, self._cmd_group)
		return self._sort

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	def clone(self) -> 'Fpeaks':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fpeaks(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
