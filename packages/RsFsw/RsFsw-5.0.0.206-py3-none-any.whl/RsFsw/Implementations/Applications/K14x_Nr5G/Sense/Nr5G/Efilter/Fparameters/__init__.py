from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fparameters:
	"""Fparameters commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fparameters", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, result: enums.ResultTypeNr5G, condition: enums.EventFilterCondition = None, value: float = None) -> None:
		"""SCPI: [SENSe]:NR5G:EFILter:FPARameters \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.efilter.fparameters.set(result = enums.ResultTypeNr5G.AAPFail, condition = enums.EventFilterCondition.FAILed, value = 1.0) \n
		This command defines a filter condition for the event filter in combined measurements. \n
			:param result: SSTate | APFail | AAPFail | ARPFail | SPFail | MID | TSTamp | TSDelta | EVM | POWer | DSQP | DSST | DSSF | DSTS | FSOFfset | PCHannel | PSIGnal | FERRor | SERRor | IQOFfset | GIMBalance | QUADrature | OSTP | RSTP | RSSI | CSIPower | SSPower | CRESt | OVLD | MODulation | NORB Selects the result that you want to define a filter for.
			:param condition: FAILed Filter condition: test failed (for boolean results only) . GTEQual Filter condition: greater than or equal (for numerical results only) . LTEQual Filter condition: lower than or equal (for numerical results only) . PASSed Filter condition: test passed (for boolean results only) .
			:param value: For numerical results only.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('result', result, DataType.Enum, enums.ResultTypeNr5G), ArgSingle('condition', condition, DataType.Enum, enums.EventFilterCondition, is_optional=True), ArgSingle('value', value, DataType.Float, None, is_optional=True))
		self._core.io.write(f'SENSe:NR5G:EFILter:FPARameters {param}'.rstrip())

	# noinspection PyTypeChecker
	class FparametersStruct(StructBase):
		"""Response structure. Fields: \n
			- Result: enums.ResultTypeNr5G: SSTate | APFail | AAPFail | ARPFail | SPFail | MID | TSTamp | TSDelta | EVM | POWer | DSQP | DSST | DSSF | DSTS | FSOFfset | PCHannel | PSIGnal | FERRor | SERRor | IQOFfset | GIMBalance | QUADrature | OSTP | RSTP | RSSI | CSIPower | SSPower | CRESt | OVLD | MODulation | NORB Selects the result that you want to define a filter for.
			- Condition: enums.EventFilterCondition: FAILed Filter condition: test failed (for boolean results only) . GTEQual Filter condition: greater than or equal (for numerical results only) . LTEQual Filter condition: lower than or equal (for numerical results only) . PASSed Filter condition: test passed (for boolean results only) .
			- Value: float: For numerical results only."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Result', enums.ResultTypeNr5G),
			ArgStruct.scalar_enum('Condition', enums.EventFilterCondition),
			ArgStruct.scalar_float('Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Result: enums.ResultTypeNr5G = None
			self.Condition: enums.EventFilterCondition = None
			self.Value: float = None

	def get(self) -> FparametersStruct:
		"""SCPI: [SENSe]:NR5G:EFILter:FPARameters \n
		Snippet: value: FparametersStruct = driver.applications.k14Xnr5G.sense.nr5G.efilter.fparameters.get() \n
		This command defines a filter condition for the event filter in combined measurements. \n
			:return: structure: for return value, see the help for FparametersStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:NR5G:EFILter:FPARameters?', self.__class__.FparametersStruct())

	def clone(self) -> 'Fparameters':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fparameters(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
