from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 18 total commands, 16 Subgroups, 0 group commands"""

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
	def nonePy(self):
		"""nonePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nonePy'):
			from .NonePy import NonePy
			self._nonePy = NonePy(self._core, self._cmd_group)
		return self._nonePy

	@property
	def hwSettings(self):
		"""hwSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hwSettings'):
			from .HwSettings import HwSettings
			self._hwSettings = HwSettings(self._core, self._cmd_group)
		return self._hwSettings

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def lines(self):
		"""lines commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lines'):
			from .Lines import Lines
			self._lines = Lines(self._core, self._cmd_group)
		return self._lines

	@property
	def csetup(self):
		"""csetup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csetup'):
			from .Csetup import Csetup
			self._csetup = Csetup(self._core, self._cmd_group)
		return self._csetup

	@property
	def cdata(self):
		"""cdata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdata'):
			from .Cdata import Cdata
			self._cdata = Cdata(self._core, self._cmd_group)
		return self._cdata

	@property
	def hardCopy(self):
		"""hardCopy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hardCopy'):
			from .HardCopy import HardCopy
			self._hardCopy = HardCopy(self._core, self._cmd_group)
		return self._hardCopy

	@property
	def macros(self):
		"""macros commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_macros'):
			from .Macros import Macros
			self._macros = Macros(self._core, self._cmd_group)
		return self._macros

	@property
	def scData(self):
		"""scData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scData'):
			from .ScData import ScData
			self._scData = ScData(self._core, self._cmd_group)
		return self._scData

	@property
	def transducer(self):
		"""transducer commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_transducer'):
			from .Transducer import Transducer
			self._transducer = Transducer(self._core, self._cmd_group)
		return self._transducer

	@property
	def spectrogram(self):
		"""spectrogram commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import Spectrogram
			self._spectrogram = Spectrogram(self._core, self._cmd_group)
		return self._spectrogram

	@property
	def final(self):
		"""final commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_final'):
			from .Final import Final
			self._final = Final(self._core, self._cmd_group)
		return self._final

	@property
	def viqData(self):
		"""viqData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_viqData'):
			from .ViqData import ViqData
			self._viqData = ViqData(self._core, self._cmd_group)
		return self._viqData

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def weighting(self):
		"""weighting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_weighting'):
			from .Weighting import Weighting
			self._weighting = Weighting(self._core, self._cmd_group)
		return self._weighting

	def clone(self) -> 'Item':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Item(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
