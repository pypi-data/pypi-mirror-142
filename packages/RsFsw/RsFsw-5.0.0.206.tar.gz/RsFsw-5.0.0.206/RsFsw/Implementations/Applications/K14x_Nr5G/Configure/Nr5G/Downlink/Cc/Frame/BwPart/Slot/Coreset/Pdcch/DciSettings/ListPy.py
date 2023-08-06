from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal.Utilities import trim_str_response
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, coreset=repcap.Coreset.Default) -> str:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:COReset<cr>:PDCCh0:DCISettings:LIST \n
		Snippet: value: str = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.coreset.pdcch.dciSettings.listPy.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, coreset = repcap.Coreset.Default) \n
		This command queries the DCI fields available for the currently selected DCI format and the number of bits each DCI field
		uses.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a DCI format .(method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Coreset.Pdcch.DciFormat.set) .
			- Assign bits to the DCI fields (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Coreset.Pdcch.DciSettings.Item.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param coreset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coreset')
			:return: list_py: String that contains the names of the DCI fields and the number of bits they use as a comma separated list."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		coreset_cmd_val = self._cmd_group.get_repcap_cmd_value(coreset, repcap.Coreset)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:COReset{coreset_cmd_val}:PDCCh0:DCISettings:LIST?')
		return trim_str_response(response)
