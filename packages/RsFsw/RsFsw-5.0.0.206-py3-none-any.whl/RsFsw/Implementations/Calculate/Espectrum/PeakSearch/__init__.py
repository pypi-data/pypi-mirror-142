from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeakSearch:
	"""PeakSearch commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peakSearch", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .Details import Details
			self._details = Details(self._core, self._cmd_group)
		return self._details

	@property
	def immediate(self):
		"""immediate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_immediate'):
			from .Immediate import Immediate
			self._immediate = Immediate(self._core, self._cmd_group)
		return self._immediate

	@property
	def margin(self):
		"""margin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_margin'):
			from .Margin import Margin
			self._margin = Margin(self._core, self._cmd_group)
		return self._margin

	@property
	def pshow(self):
		"""pshow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pshow'):
			from .Pshow import Pshow
			self._pshow = Pshow(self._core, self._cmd_group)
		return self._pshow

	def clone(self) -> 'PeakSearch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PeakSearch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
