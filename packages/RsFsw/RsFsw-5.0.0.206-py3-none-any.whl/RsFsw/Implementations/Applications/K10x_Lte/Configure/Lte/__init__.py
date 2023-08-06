from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 174 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	@property
	def antMatrix(self):
		"""antMatrix commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_antMatrix'):
			from .AntMatrix import AntMatrix
			self._antMatrix = AntMatrix(self._core, self._cmd_group)
		return self._antMatrix

	@property
	def caggregation(self):
		"""caggregation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caggregation'):
			from .Caggregation import Caggregation
			self._caggregation = Caggregation(self._core, self._cmd_group)
		return self._caggregation

	@property
	def downlink(self):
		"""downlink commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def duplexing(self):
		"""duplexing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duplexing'):
			from .Duplexing import Duplexing
			self._duplexing = Duplexing(self._core, self._cmd_group)
		return self._duplexing

	@property
	def eutra(self):
		"""eutra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eutra'):
			from .Eutra import Eutra
			self._eutra = Eutra(self._core, self._cmd_group)
		return self._eutra

	@property
	def ldirection(self):
		"""ldirection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldirection'):
			from .Ldirection import Ldirection
			self._ldirection = Ldirection(self._core, self._cmd_group)
		return self._ldirection

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	@property
	def mimo(self):
		"""mimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	@property
	def ndevices(self):
		"""ndevices commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndevices'):
			from .Ndevices import Ndevices
			self._ndevices = Ndevices(self._core, self._cmd_group)
		return self._ndevices

	@property
	def noCc(self):
		"""noCc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noCc'):
			from .NoCc import NoCc
			self._noCc = NoCc(self._core, self._cmd_group)
		return self._noCc

	@property
	def ooPower(self):
		"""ooPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ooPower'):
			from .OoPower import OoPower
			self._ooPower = OoPower(self._core, self._cmd_group)
		return self._ooPower

	@property
	def oran(self):
		"""oran commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_oran'):
			from .Oran import Oran
			self._oran = Oran(self._core, self._cmd_group)
		return self._oran

	@property
	def uplink(self):
		"""uplink commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import Uplink
			self._uplink = Uplink(self._core, self._cmd_group)
		return self._uplink

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Lte':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lte(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
