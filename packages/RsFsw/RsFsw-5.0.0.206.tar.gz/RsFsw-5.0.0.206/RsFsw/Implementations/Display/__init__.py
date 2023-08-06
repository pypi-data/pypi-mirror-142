from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 86 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	@property
	def window(self):
		"""window commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	@property
	def minfo(self):
		"""minfo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_minfo'):
			from .Minfo import Minfo
			self._minfo = Minfo(self._core, self._cmd_group)
		return self._minfo

	@property
	def wselect(self):
		"""wselect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wselect'):
			from .Wselect import Wselect
			self._wselect = Wselect(self._core, self._cmd_group)
		return self._wselect

	@property
	def annotation(self):
		"""annotation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_annotation'):
			from .Annotation import Annotation
			self._annotation = Annotation(self._core, self._cmd_group)
		return self._annotation

	@property
	def atab(self):
		"""atab commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atab'):
			from .Atab import Atab
			self._atab = Atab(self._core, self._cmd_group)
		return self._atab

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def logo(self):
		"""logo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_logo'):
			from .Logo import Logo
			self._logo = Logo(self._core, self._cmd_group)
		return self._logo

	@property
	def theme(self):
		"""theme commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_theme'):
			from .Theme import Theme
			self._theme = Theme(self._core, self._cmd_group)
		return self._theme

	@property
	def cmap(self):
		"""cmap commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmap'):
			from .Cmap import Cmap
			self._cmap = Cmap(self._core, self._cmd_group)
		return self._cmap

	@property
	def faccess(self):
		"""faccess commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_faccess'):
			from .Faccess import Faccess
			self._faccess = Faccess(self._core, self._cmd_group)
		return self._faccess

	@property
	def preSelector(self):
		"""preSelector commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preSelector'):
			from .PreSelector import PreSelector
			self._preSelector = PreSelector(self._core, self._cmd_group)
		return self._preSelector

	@property
	def touchscreen(self):
		"""touchscreen commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_touchscreen'):
			from .Touchscreen import Touchscreen
			self._touchscreen = Touchscreen(self._core, self._cmd_group)
		return self._touchscreen

	@property
	def tbar(self):
		"""tbar commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tbar'):
			from .Tbar import Tbar
			self._tbar = Tbar(self._core, self._cmd_group)
		return self._tbar

	@property
	def sbar(self):
		"""sbar commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sbar'):
			from .Sbar import Sbar
			self._sbar = Sbar(self._core, self._cmd_group)
		return self._sbar

	@property
	def skeys(self):
		"""skeys commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_skeys'):
			from .Skeys import Skeys
			self._skeys = Skeys(self._core, self._cmd_group)
		return self._skeys

	@property
	def iterm(self):
		"""iterm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iterm'):
			from .Iterm import Iterm
			self._iterm = Iterm(self._core, self._cmd_group)
		return self._iterm

	@property
	def blighting(self):
		"""blighting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blighting'):
			from .Blighting import Blighting
			self._blighting = Blighting(self._core, self._cmd_group)
		return self._blighting

	def clone(self) -> 'Display':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Display(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
