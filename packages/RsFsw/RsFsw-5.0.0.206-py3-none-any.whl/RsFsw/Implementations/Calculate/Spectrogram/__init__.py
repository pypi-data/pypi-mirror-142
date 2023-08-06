from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrogram:
	"""Spectrogram commands group definition. 10 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrogram", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def threeDim(self):
		"""threeDim commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_threeDim'):
			from .ThreeDim import ThreeDim
			self._threeDim = ThreeDim(self._core, self._cmd_group)
		return self._threeDim

	@property
	def hdepth(self):
		"""hdepth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hdepth'):
			from .Hdepth import Hdepth
			self._hdepth = Hdepth(self._core, self._cmd_group)
		return self._hdepth

	@property
	def color(self):
		"""color commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_color'):
			from .Color import Color
			self._color = Color(self._core, self._cmd_group)
		return self._color

	@property
	def tstamp(self):
		"""tstamp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import Tstamp
			self._tstamp = Tstamp(self._core, self._cmd_group)
		return self._tstamp

	@property
	def frame(self):
		"""frame commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def continuous(self):
		"""continuous commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_continuous'):
			from .Continuous import Continuous
			self._continuous = Continuous(self._core, self._cmd_group)
		return self._continuous

	@property
	def clear(self):
		"""clear commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import Clear
			self._clear = Clear(self._core, self._cmd_group)
		return self._clear

	def clone(self) -> 'Spectrogram':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spectrogram(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
