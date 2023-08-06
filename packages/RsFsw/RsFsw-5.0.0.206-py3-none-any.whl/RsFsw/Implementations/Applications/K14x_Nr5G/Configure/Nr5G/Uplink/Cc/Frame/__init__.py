from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 109 total commands, 3 Subgroups, 1 group commands
	Repeated Capability: Frame, default value after init: Frame.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_frame_get', 'repcap_frame_set', repcap.Frame.Nr1)

	def repcap_frame_set(self, frame: repcap.Frame) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Frame.Default
		Default value after init: Frame.Nr1"""
		self._cmd_group.set_repcap_enum_value(frame)

	def repcap_frame_get(self) -> repcap.Frame:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bwPart(self):
		"""bwPart commands group. 11 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwPart'):
			from .BwPart import BwPart
			self._bwPart = BwPart(self._core, self._cmd_group)
		return self._bwPart

	@property
	def bwpCount(self):
		"""bwpCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwpCount'):
			from .BwpCount import BwpCount
			self._bwpCount = BwpCount(self._core, self._cmd_group)
		return self._bwpCount

	@property
	def paste(self):
		"""paste commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_paste'):
			from .Paste import Paste
			self._paste = Paste(self._core, self._cmd_group)
		return self._paste

	def copy(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:COPY \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.copy(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default) \n
		This command copies a frame configuration. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
		"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:COPY')

	def copy_with_opc(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, opc_timeout_ms: int = -1) -> None:
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:COPY \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.copy_with_opc(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default) \n
		This command copies a frame configuration. \n
		Same as copy, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:COPY', opc_timeout_ms)

	def clone(self) -> 'Frame':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frame(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
