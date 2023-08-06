from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gos:
	"""Gos commands group definition. 12 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gos", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def crest(self):
		"""crest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import Crest
			self._crest = Crest(self._core, self._cmd_group)
		return self._crest

	@property
	def dcycle(self):
		"""dcycle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import Dcycle
			self._dcycle = Dcycle(self._core, self._cmd_group)
		return self._dcycle

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	@property
	def nposition(self):
		"""nposition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nposition'):
			from .Nposition import Nposition
			self._nposition = Nposition(self._core, self._cmd_group)
		return self._nposition

	@property
	def nwidth(self):
		"""nwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nwidth'):
			from .Nwidth import Nwidth
			self._nwidth = Nwidth(self._core, self._cmd_group)
		return self._nwidth

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import Rlength
			self._rlength = Rlength(self._core, self._cmd_group)
		return self._rlength

	@property
	def slength(self):
		"""slength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import Slength
			self._slength = Slength(self._core, self._cmd_group)
		return self._slength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def wname(self):
		"""wname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wname'):
			from .Wname import Wname
			self._wname = Wname(self._core, self._cmd_group)
		return self._wname

	@property
	def write(self):
		"""write commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_write'):
			from .Write import Write
			self._write = Write(self._core, self._cmd_group)
		return self._write

	def clone(self) -> 'Gos':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gos(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
