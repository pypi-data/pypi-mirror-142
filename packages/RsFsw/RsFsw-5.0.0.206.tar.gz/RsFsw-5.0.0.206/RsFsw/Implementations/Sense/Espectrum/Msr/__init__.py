from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msr:
	"""Msr commands group definition. 9 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msr", core, parent)

	@property
	def rfbWidth(self):
		"""rfbWidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfbWidth'):
			from .RfbWidth import RfbWidth
			self._rfbWidth = RfbWidth(self._core, self._cmd_group)
		return self._rfbWidth

	@property
	def bcategory(self):
		"""bcategory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bcategory'):
			from .Bcategory import Bcategory
			self._bcategory = Bcategory(self._core, self._cmd_group)
		return self._bcategory

	@property
	def mpower(self):
		"""mpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpower'):
			from .Mpower import Mpower
			self._mpower = Mpower(self._core, self._cmd_group)
		return self._mpower

	@property
	def classPy(self):
		"""classPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_classPy'):
			from .ClassPy import ClassPy
			self._classPy = ClassPy(self._core, self._cmd_group)
		return self._classPy

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .Band import Band
			self._band = Band(self._core, self._cmd_group)
		return self._band

	@property
	def gsm(self):
		"""gsm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gsm'):
			from .Gsm import Gsm
			self._gsm = Gsm(self._core, self._cmd_group)
		return self._gsm

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import Lte
			self._lte = Lte(self._core, self._cmd_group)
		return self._lte

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	def clone(self) -> 'Msr':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Msr(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
