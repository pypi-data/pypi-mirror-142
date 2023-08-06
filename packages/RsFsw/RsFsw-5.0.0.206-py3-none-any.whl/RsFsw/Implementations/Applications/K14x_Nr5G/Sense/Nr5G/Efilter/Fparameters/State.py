from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, result: enums.ResultTypeNr5G, state: bool) -> None:
		"""SCPI: [SENSe]:NR5G:EFILter:FPARameters:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.efilter.fparameters.state.set(result = enums.ResultTypeNr5G.AAPFail, state = False) \n
		This command turns an event filter on and off. Turning on an event filter adds it to the filter list and removes the
		results from the result summary that do not fulfill the filter conditions. Turning it off removes it from the list.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Define a filter condition ([SENSe:]NR5G:EFILter:FPARameters) . \n
			:param result: CRESt | DSQP | DSSF | DSST | DSTS | FSOFfset | EVM | OVLD | FERRor | GIMBalance | IQOFfset | MODulation | NORB | OSTP | RSTP | RSSI | SSPower | CSIPower | PCHannel | POWer | PPRE | PSIGnal | QUADrature | SERRor | MID | TSTamp | TSDelta | SSTate | APFail | AAPFail | ARPFail | SPFail Selects the result that you want to add a filter for.
			:param state: ON | OFF | 1 | 0
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('result', result, DataType.Enum, enums.ResultTypeNr5G), ArgSingle('state', state, DataType.Boolean))
		self._core.io.write(f'SENSe:NR5G:EFILter:FPARameters:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Result: enums.ResultTypeNr5G: CRESt | DSQP | DSSF | DSST | DSTS | FSOFfset | EVM | OVLD | FERRor | GIMBalance | IQOFfset | MODulation | NORB | OSTP | RSTP | RSSI | SSPower | CSIPower | PCHannel | POWer | PPRE | PSIGnal | QUADrature | SERRor | MID | TSTamp | TSDelta | SSTate | APFail | AAPFail | ARPFail | SPFail Selects the result that you want to add a filter for.
			- State: bool: ON | OFF | 1 | 0"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Result', enums.ResultTypeNr5G),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Result: enums.ResultTypeNr5G = None
			self.State: bool = None

	def get(self) -> StateStruct:
		"""SCPI: [SENSe]:NR5G:EFILter:FPARameters:STATe \n
		Snippet: value: StateStruct = driver.applications.k14Xnr5G.sense.nr5G.efilter.fparameters.state.get() \n
		This command turns an event filter on and off. Turning on an event filter adds it to the filter list and removes the
		results from the result summary that do not fulfill the filter conditions. Turning it off removes it from the list.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Define a filter condition ([SENSe:]NR5G:EFILter:FPARameters) . \n
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:NR5G:EFILter:FPARameters:STATe?', self.__class__.StateStruct())
