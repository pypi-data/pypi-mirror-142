from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Item:
	"""Item commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("item", core, parent)

	def set(self, result: enums.ResultTypeNr5G, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: driver.applications.k14Xnr5G.display.window.table.item.set(result = enums.ResultTypeNr5G.AAPFail, state = False, window = repcap.Window.Default) \n
		This command turns the display of individual results in the numerical result summary on and off. \n
			:param result: CRESt | DSQP | DSSF | DSST | DSTS | UPRach | FSOFfset | EVM | EVMPeak | FERRor | GIMBalance | IQOFfset | MODulation | NORB | OSTP | RSTP | SSPower | CSIPower | PCHannel | POWer | PPRE | PSIGnal | QUADrature | SDPB | SDQP | SDSF | SDST | SDTS | SERRor | UCCD | UCCH | USPB | USQP | USSF | USST | USTS Combined measurements only: TSTamp | TSDelta | MID | SSTate | APFail | AAPFail |ARPFail | SPFail
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('result', result, DataType.Enum, enums.ResultTypeNr5G), ArgSingle('state', state, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM {param}'.rstrip())

	# noinspection PyTypeChecker
	class ItemStruct(StructBase):
		"""Response structure. Fields: \n
			- Result: enums.ResultTypeNr5G: CRESt | DSQP | DSSF | DSST | DSTS | UPRach | FSOFfset | EVM | EVMPeak | FERRor | GIMBalance | IQOFfset | MODulation | NORB | OSTP | RSTP | SSPower | CSIPower | PCHannel | POWer | PPRE | PSIGnal | QUADrature | SDPB | SDQP | SDSF | SDST | SDTS | SERRor | UCCD | UCCH | USPB | USQP | USSF | USST | USTS Combined measurements only: TSTamp | TSDelta | MID | SSTate | APFail | AAPFail |ARPFail | SPFail
			- State: bool: ON | OFF | 1 | 0"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Result', enums.ResultTypeNr5G),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Result: enums.ResultTypeNr5G = None
			self.State: bool = None

	def get(self, window=repcap.Window.Default) -> ItemStruct:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe:ITEM \n
		Snippet: value: ItemStruct = driver.applications.k14Xnr5G.display.window.table.item.get(window = repcap.Window.Default) \n
		This command turns the display of individual results in the numerical result summary on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: structure: for return value, see the help for ItemStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'DISPlay:WINDow{window_cmd_val}:TABLe:ITEM?', self.__class__.ItemStruct())
