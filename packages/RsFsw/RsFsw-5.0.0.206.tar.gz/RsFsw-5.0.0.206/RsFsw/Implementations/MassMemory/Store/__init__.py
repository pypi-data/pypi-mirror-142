from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 19 total commands, 13 Subgroups, 0 group commands
	Repeated Capability: Store, default value after init: Store.Pos1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_store_get', 'repcap_store_set', repcap.Store.Pos1)

	def repcap_store_set(self, store: repcap.Store) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Store.Default
		Default value after init: Store.Pos1"""
		self._cmd_group.set_repcap_enum_value(store)

	def repcap_store_get(self) -> repcap.Store:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def iq(self):
		"""iq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def table(self):
		"""table commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	@property
	def wav(self):
		"""wav commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_wav'):
			from .Wav import Wav
			self._wav = Wav(self._core, self._cmd_group)
		return self._wav

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def spurious(self):
		"""spurious commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spurious'):
			from .Spurious import Spurious
			self._spurious = Spurious(self._core, self._cmd_group)
		return self._spurious

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def spectrogram(self):
		"""spectrogram commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import Spectrogram
			self._spectrogram = Spectrogram(self._core, self._cmd_group)
		return self._spectrogram

	@property
	def pspectrum(self):
		"""pspectrum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pspectrum'):
			from .Pspectrum import Pspectrum
			self._pspectrum = Pspectrum(self._core, self._cmd_group)
		return self._pspectrum

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def tfactor(self):
		"""tfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tfactor'):
			from .Tfactor import Tfactor
			self._tfactor = Tfactor(self._core, self._cmd_group)
		return self._tfactor

	def clone(self) -> 'Store':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Store(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
