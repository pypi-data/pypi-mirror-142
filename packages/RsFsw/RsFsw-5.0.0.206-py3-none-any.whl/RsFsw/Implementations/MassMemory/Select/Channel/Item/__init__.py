from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

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
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def hwSettings(self):
		"""hwSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hwSettings'):
			from .HwSettings import HwSettings
			self._hwSettings = HwSettings(self._core, self._cmd_group)
		return self._hwSettings

	@property
	def lines(self):
		"""lines commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lines'):
			from .Lines import Lines
			self._lines = Lines(self._core, self._cmd_group)
		return self._lines

	@property
	def scData(self):
		"""scData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scData'):
			from .ScData import ScData
			self._scData = ScData(self._core, self._cmd_group)
		return self._scData

	@property
	def spectrogram(self):
		"""spectrogram commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import Spectrogram
			self._spectrogram = Spectrogram(self._core, self._cmd_group)
		return self._spectrogram

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def transducer(self):
		"""transducer commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_transducer'):
			from .Transducer import Transducer
			self._transducer = Transducer(self._core, self._cmd_group)
		return self._transducer

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
