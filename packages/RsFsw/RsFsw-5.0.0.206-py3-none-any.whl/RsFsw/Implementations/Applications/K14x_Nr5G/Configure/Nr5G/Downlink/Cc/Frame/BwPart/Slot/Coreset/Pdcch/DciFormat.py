from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import enums
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciFormat:
	"""DciFormat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciFormat", core, parent)

	def set(self, format_py: enums.FormatDci, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, coreset=repcap.Coreset.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:COReset<cr>:PDCCh0:DCIFormat \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.coreset.pdcch.dciFormat.set(format_py = enums.FormatDci.F00, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, coreset = repcap.Coreset.Default) \n
		This command selects the DCI format for a PDCCH.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- The availability of DCI formats depends on the selected RNTI type (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Coreset.Pdcch.Usage.set) . \n
			:param format_py: F00 | F01 | F02 | F10 | F11 | F12 | F20 | F21 | F22 | F23 | F24 | F25 | F26
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param coreset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coreset')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.FormatDci)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		coreset_cmd_val = self._cmd_group.get_repcap_cmd_value(coreset, repcap.Coreset)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:COReset{coreset_cmd_val}:PDCCh0:DCIFormat {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, coreset=repcap.Coreset.Default) -> enums.FormatDci:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:COReset<cr>:PDCCh0:DCIFormat \n
		Snippet: value: enums.FormatDci = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.coreset.pdcch.dciFormat.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, coreset = repcap.Coreset.Default) \n
		This command selects the DCI format for a PDCCH.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- The availability of DCI formats depends on the selected RNTI type (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Coreset.Pdcch.Usage.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param coreset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coreset')
			:return: format_py: F00 | F01 | F02 | F10 | F11 | F12 | F20 | F21 | F22 | F23 | F24 | F25 | F26"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		coreset_cmd_val = self._cmd_group.get_repcap_cmd_value(coreset, repcap.Coreset)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:COReset{coreset_cmd_val}:PDCCh0:DCIFormat?')
		return Conversions.str_to_scalar_enum(response, enums.FormatDci)
