from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Achannel:
	"""Achannel commands group definition. 69 total commands, 16 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	@property
	def aaChannel(self):
		"""aaChannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aaChannel'):
			from .AaChannel import AaChannel
			self._aaChannel = AaChannel(self._core, self._cmd_group)
		return self._aaChannel

	@property
	def acPairs(self):
		"""acPairs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acPairs'):
			from .AcPairs import AcPairs
			self._acPairs = AcPairs(self._core, self._cmd_group)
		return self._acPairs

	@property
	def agChannels(self):
		"""agChannels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_agChannels'):
			from .AgChannels import AgChannels
			self._agChannels = AgChannels(self._core, self._cmd_group)
		return self._agChannels

	@property
	def bandwidth(self):
		"""bandwidth commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def gap(self):
		"""gap commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_gap'):
			from .Gap import Gap
			self._gap = Gap(self._core, self._cmd_group)
		return self._gap

	@property
	def gchannel(self):
		"""gchannel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gchannel'):
			from .Gchannel import Gchannel
			self._gchannel = Gchannel(self._core, self._cmd_group)
		return self._gchannel

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def name(self):
		"""name commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def preset(self):
		"""preset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import Preset
			self._preset = Preset(self._core, self._cmd_group)
		return self._preset

	@property
	def reference(self):
		"""reference commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	@property
	def sbcount(self):
		"""sbcount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbcount'):
			from .Sbcount import Sbcount
			self._sbcount = Sbcount(self._core, self._cmd_group)
		return self._sbcount

	@property
	def sblock(self):
		"""sblock commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_sblock'):
			from .Sblock import Sblock
			self._sblock = Sblock(self._core, self._cmd_group)
		return self._sblock

	@property
	def spacing(self):
		"""spacing commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_spacing'):
			from .Spacing import Spacing
			self._spacing = Spacing(self._core, self._cmd_group)
		return self._spacing

	@property
	def ssetup(self):
		"""ssetup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssetup'):
			from .Ssetup import Ssetup
			self._ssetup = Ssetup(self._core, self._cmd_group)
		return self._ssetup

	@property
	def txChannel(self):
		"""txChannel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_txChannel'):
			from .TxChannel import TxChannel
			self._txChannel = TxChannel(self._core, self._cmd_group)
		return self._txChannel

	def preset_execute(self, measurement: enums.PowerMeasFunctionB) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:PRESet \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.preset_execute(measurement = enums.PowerMeasFunctionB.ACPower) \n
		No command help available \n
			:param measurement: No help available
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.PowerMeasFunctionB)
		self._core.io.write(f'SENSe:POWer:ACHannel:PRESet {param}')

	def clone(self) -> 'Achannel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Achannel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
