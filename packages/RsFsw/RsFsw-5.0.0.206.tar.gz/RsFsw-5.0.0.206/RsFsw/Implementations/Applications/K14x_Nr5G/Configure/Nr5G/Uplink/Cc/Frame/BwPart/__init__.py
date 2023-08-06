from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwPart:
	"""BwPart commands group definition. 105 total commands, 11 Subgroups, 1 group commands
	Repeated Capability: BwPart, default value after init: BwPart.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwPart", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_bwPart_get', 'repcap_bwPart_set', repcap.BwPart.Nr1)

	def repcap_bwPart_set(self, bwPart: repcap.BwPart) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to BwPart.Default
		Default value after init: BwPart.Nr1"""
		self._cmd_group.set_repcap_enum_value(bwPart)

	def repcap_bwPart_get(self) -> repcap.BwPart:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def cslot(self):
		"""cslot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cslot'):
			from .Cslot import Cslot
			self._cslot = Cslot(self._core, self._cmd_group)
		return self._cslot

	@property
	def detection(self):
		"""detection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detection'):
			from .Detection import Detection
			self._detection = Detection(self._core, self._cmd_group)
		return self._detection

	@property
	def duplicate(self):
		"""duplicate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duplicate'):
			from .Duplicate import Duplicate
			self._duplicate = Duplicate(self._core, self._cmd_group)
		return self._duplicate

	@property
	def rbCount(self):
		"""rbCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbCount'):
			from .RbCount import RbCount
			self._rbCount = RbCount(self._core, self._cmd_group)
		return self._rbCount

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def remove(self):
		"""remove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import Remove
			self._remove = Remove(self._core, self._cmd_group)
		return self._remove

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import Scount
			self._scount = Scount(self._core, self._cmd_group)
		return self._scount

	@property
	def slot(self):
		"""slot commands group. 8 Sub-classes, 2 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def srs(self):
		"""srs commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_srs'):
			from .Srs import Srs
			self._srs = Srs(self._core, self._cmd_group)
		return self._srs

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import Sspacing
			self._sspacing = Sspacing(self._core, self._cmd_group)
		return self._sspacing

	def clear(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CLEar \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.clear(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command deletes all bandwidth parts. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
		"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CLEar')

	def clear_with_opc(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, opc_timeout_ms: int = -1) -> None:
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CLEar \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.clear_with_opc(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command deletes all bandwidth parts. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CLEar', opc_timeout_ms)

	def clone(self) -> 'BwPart':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BwPart(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
