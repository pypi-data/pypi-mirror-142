from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 14 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def data(self):
		"""data commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import Rlength
			self._rlength = Rlength(self._core, self._cmd_group)
		return self._rlength

	@property
	def synchronized(self):
		"""synchronized commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronized'):
			from .Synchronized import Synchronized
			self._synchronized = Synchronized(self._core, self._cmd_group)
		return self._synchronized

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def equalized(self):
		"""equalized commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_equalized'):
			from .Equalized import Equalized
			self._equalized = Equalized(self._core, self._cmd_group)
		return self._equalized

	@property
	def tpis(self):
		"""tpis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpis'):
			from .Tpis import Tpis
			self._tpis = Tpis(self._core, self._cmd_group)
		return self._tpis

	@property
	def symbolRate(self):
		"""symbolRate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def wband(self):
		"""wband commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wband'):
			from .Wband import Wband
			self._wband = Wband(self._core, self._cmd_group)
		return self._wband

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
