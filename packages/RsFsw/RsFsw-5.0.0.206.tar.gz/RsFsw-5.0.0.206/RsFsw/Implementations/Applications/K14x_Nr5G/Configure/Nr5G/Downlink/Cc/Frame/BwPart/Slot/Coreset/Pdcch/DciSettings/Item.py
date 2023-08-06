from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal.Types import DataType
from ..............Internal.StructBase import StructBase
from ..............Internal.ArgStruct import ArgStruct
from ..............Internal.ArgSingleList import ArgSingleList
from ..............Internal.ArgSingle import ArgSingle
from .............. import enums
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	def set(self, dci_field: enums.DciField, bit_length: float, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, coreset=repcap.Coreset.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:COReset<cr>:PDCCh0:DCISettings:ITEM \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.coreset.pdcch.dciSettings.item.set(dci_field = enums.DciField.AINDicator, bit_length = 1.0, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, coreset = repcap.Coreset.Default) \n
		This command defines the bit length for DCI fields.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Availability of parameters depend on the selected DCI format (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Coreset.Pdcch.DciFormat.set) .
		Note that, depending on the DCI format, some bit lengths are fix and cannot be changed. \n
			:param dci_field: For an overview of parameters, see Table 'List of DCI fields'.
			:param bit_length: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param coreset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coreset')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dci_field', dci_field, DataType.Enum, enums.DciField), ArgSingle('bit_length', bit_length, DataType.Float))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		coreset_cmd_val = self._cmd_group.get_repcap_cmd_value(coreset, repcap.Coreset)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:COReset{coreset_cmd_val}:PDCCh0:DCISettings:ITEM {param}'.rstrip())

	# noinspection PyTypeChecker
	class ItemStruct(StructBase):
		"""Response structure. Fields: \n
			- Dci_Field: enums.DciField: For an overview of parameters, see Table 'List of DCI fields'.
			- Bit_Length: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Dci_Field', enums.DciField),
			ArgStruct.scalar_float('Bit_Length')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dci_Field: enums.DciField = None
			self.Bit_Length: float = None

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, coreset=repcap.Coreset.Default) -> ItemStruct:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:COReset<cr>:PDCCh0:DCISettings:ITEM \n
		Snippet: value: ItemStruct = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.coreset.pdcch.dciSettings.item.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, coreset = repcap.Coreset.Default) \n
		This command defines the bit length for DCI fields.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Availability of parameters depend on the selected DCI format (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Coreset.Pdcch.DciFormat.set) .
		Note that, depending on the DCI format, some bit lengths are fix and cannot be changed. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param coreset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Coreset')
			:return: structure: for return value, see the help for ItemStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		coreset_cmd_val = self._cmd_group.get_repcap_cmd_value(coreset, repcap.Coreset)
		return self._core.io.query_struct(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:COReset{coreset_cmd_val}:PDCCh0:DCISettings:ITEM?', self.__class__.ItemStruct())
