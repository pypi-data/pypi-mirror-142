from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, value: float, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:PASTe:TO:DURation \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.paste.to.duration.set(value = 1.0, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default) \n
		This command defines to which slots a slot configuration is copied to.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- A slot configuration is in the clipboard (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.copy) .
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Cslot.set) .
			- Select custom paste mode (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Paste.To.Mode.set) . \n
			:param value: The paste duration corresponds to a certain number of slots in a row.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.decimal_value_to_str(value)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:PASTe:TO:DURation {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:PASTe:TO:DURation \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.paste.to.duration.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default) \n
		This command defines to which slots a slot configuration is copied to.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- A slot configuration is in the clipboard (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.copy) .
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Cslot.set) .
			- Select custom paste mode (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Paste.To.Mode.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: value: The paste duration corresponds to a certain number of slots in a row."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:PASTe:TO:DURation?')
		return Conversions.str_to_float(response)
