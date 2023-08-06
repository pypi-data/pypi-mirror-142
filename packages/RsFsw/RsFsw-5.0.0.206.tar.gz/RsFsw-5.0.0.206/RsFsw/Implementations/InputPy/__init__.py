from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 58 total commands, 17 Subgroups, 0 group commands
	Repeated Capability: InputIx, default value after init: InputIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_inputIx_get', 'repcap_inputIx_set', repcap.InputIx.Nr1)

	def repcap_inputIx_set(self, inputIx: repcap.InputIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to InputIx.Default
		Default value after init: InputIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(inputIx)

	def repcap_inputIx_get(self) -> repcap.InputIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def connector(self):
		"""connector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_connector'):
			from .Connector import Connector
			self._connector = Connector(self._core, self._cmd_group)
		return self._connector

	@property
	def attenuation(self):
		"""attenuation commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_attenuation'):
			from .Attenuation import Attenuation
			self._attenuation = Attenuation(self._core, self._cmd_group)
		return self._attenuation

	@property
	def impedance(self):
		"""impedance commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_impedance'):
			from .Impedance import Impedance
			self._impedance = Impedance(self._core, self._cmd_group)
		return self._impedance

	@property
	def mixer(self):
		"""mixer commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import Mixer
			self._mixer = Mixer(self._core, self._cmd_group)
		return self._mixer

	@property
	def uport(self):
		"""uport commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_uport'):
			from .Uport import Uport
			self._uport = Uport(self._core, self._cmd_group)
		return self._uport

	@property
	def lisn(self):
		"""lisn commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lisn'):
			from .Lisn import Lisn
			self._lisn = Lisn(self._core, self._cmd_group)
		return self._lisn

	@property
	def egain(self):
		"""egain commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_egain'):
			from .Egain import Egain
			self._egain = Egain(self._core, self._cmd_group)
		return self._egain

	@property
	def iq(self):
		"""iq commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def file(self):
		"""file commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def terminator(self):
		"""terminator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_terminator'):
			from .Terminator import Terminator
			self._terminator = Terminator(self._core, self._cmd_group)
		return self._terminator

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import Coupling
			self._coupling = Coupling(self._core, self._cmd_group)
		return self._coupling

	@property
	def diq(self):
		"""diq commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_diq'):
			from .Diq import Diq
			self._diq = Diq(self._core, self._cmd_group)
		return self._diq

	@property
	def dpath(self):
		"""dpath commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpath'):
			from .Dpath import Dpath
			self._dpath = Dpath(self._core, self._cmd_group)
		return self._dpath

	@property
	def eatt(self):
		"""eatt commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_eatt'):
			from .Eatt import Eatt
			self._eatt = Eatt(self._core, self._cmd_group)
		return self._eatt

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def gain(self):
		"""gain commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
