from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 19 total commands, 13 Subgroups, 1 group commands
	Repeated Capability: RangePy, default value after init: RangePy.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rangePy_get', 'repcap_rangePy_set', repcap.RangePy.Ix1)

	def repcap_rangePy_set(self, rangePy: repcap.RangePy) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RangePy.Default
		Default value after init: RangePy.Ix1"""
		self._cmd_group.set_repcap_enum_value(rangePy)

	def repcap_rangePy_get(self) -> repcap.RangePy:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bandwidth(self):
		"""bandwidth commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def uaRange(self):
		"""uaRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uaRange'):
			from .UaRange import UaRange
			self._uaRange = UaRange(self._core, self._cmd_group)
		return self._uaRange

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def inputPy(self):
		"""inputPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def mfRbw(self):
		"""mfRbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mfRbw'):
			from .MfRbw import MfRbw
			self._mfRbw = MfRbw(self._core, self._cmd_group)
		return self._mfRbw

	@property
	def loffset(self):
		"""loffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loffset'):
			from .Loffset import Loffset
			self._loffset = Loffset(self._core, self._cmd_group)
		return self._loffset

	@property
	def nfft(self):
		"""nfft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nfft'):
			from .Nfft import Nfft
			self._nfft = Nfft(self._core, self._cmd_group)
		return self._nfft

	@property
	def pexcursion(self):
		"""pexcursion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexcursion'):
			from .Pexcursion import Pexcursion
			self._pexcursion = Pexcursion(self._core, self._cmd_group)
		return self._pexcursion

	@property
	def refLevel(self):
		"""refLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevel
			self._refLevel = RefLevel(self._core, self._cmd_group)
		return self._refLevel

	@property
	def snRatio(self):
		"""snRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snRatio'):
			from .SnRatio import SnRatio
			self._snRatio = SnRatio(self._core, self._cmd_group)
		return self._snRatio

	@property
	def threshold(self):
		"""threshold commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_threshold'):
			from .Threshold import Threshold
			self._threshold = Threshold(self._core, self._cmd_group)
		return self._threshold

	def delete(self, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:DELete \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.delete(rangePy = repcap.RangePy.Default) \n
		No command help available \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:DELete')

	def delete_with_opc(self, rangePy=repcap.RangePy.Default, opc_timeout_ms: int = -1) -> None:
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		"""SCPI: [SENSe]:LIST:RANGe<ri>:DELete \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.delete_with_opc(rangePy = repcap.RangePy.Default) \n
		No command help available \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:LIST:RANGe{rangePy_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'Range':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Range(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
