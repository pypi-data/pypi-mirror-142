from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Sample_Rate: float: numeric value The frequency at which measurement values are taken from the A/D-converter and stored in I/Q memory. Allowed range: refer to 'Sample rate and demodulation bandwidth'. Unit: HZ
			- Record_Length: float: Number of samples to be stored in I/Q memory. Range: 1 to 400001 with AF filter or AF trigger active, 1 to 480001 with both AF filter and AF trigger deactive
			- Trigger_Source: enums.TriggerSourceB: Selection of the trigger source to use for the demodulator. For details on trigger sources see 'Trigger Source'. IMMediate | EXTernal | EXT2 | EXT3 | IFPower | RFPower| AF | AM | AMRelative | FM | PM Note: After selecting IF Power, the trigger threshold can be set with the [CMDLINK: TRIGger[:SEQuence]:LEVel:IFPower CMDLINK] command.
			- Trigger_Slope: enums.SlopeType: POSitive | NEGative Used slope of the trigger signal. The value indicated here will be ignored for trigger source = IMMediate.
			- Offset_Samples: float: Number of samples to be used as an offset to the trigger signal. For details refer to 'Sample rate and demodulation bandwidth'. The value indicated here is ignored for trigger source = 'IMMediate'.
			- No_Of_Meas: float: Number of repetitions of the measurement to be executed. The value indicated here is especially necessary for the average/maxhold/minhold function. Range: 0 to 32767"""
		__meta_args_list = [
			ArgStruct.scalar_float('Sample_Rate'),
			ArgStruct.scalar_float('Record_Length'),
			ArgStruct.scalar_enum('Trigger_Source', enums.TriggerSourceB),
			ArgStruct.scalar_enum('Trigger_Slope', enums.SlopeType),
			ArgStruct.scalar_float('Offset_Samples'),
			ArgStruct.scalar_float('No_Of_Meas')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sample_Rate: float = None
			self.Record_Length: float = None
			self.Trigger_Source: enums.TriggerSourceB = None
			self.Trigger_Slope: enums.SlopeType = None
			self.Offset_Samples: float = None
			self.No_Of_Meas: float = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [SENSe]:ADEMod:SET \n
		Snippet with structure: \n
		structure = driver.sense.ademod.set.SetStruct() \n
		structure.Sample_Rate: float = 1.0 \n
		structure.Record_Length: float = 1.0 \n
		structure.Trigger_Source: enums.TriggerSourceB = enums.TriggerSourceB.ACVideo \n
		structure.Trigger_Slope: enums.SlopeType = enums.SlopeType.NEGative \n
		structure.Offset_Samples: float = 1.0 \n
		structure.No_Of_Meas: float = 1.0 \n
		driver.sense.ademod.set.set(structure) \n
		This command configures the analog demodulator of the instrument. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'SENSe:ADEMod:SET', structure)

	def get(self) -> SetStruct:
		"""SCPI: [SENSe]:ADEMod:SET \n
		Snippet: value: SetStruct = driver.sense.ademod.set.get() \n
		This command configures the analog demodulator of the instrument. \n
			:return: structure: for return value, see the help for SetStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:ADEMod:SET?', self.__class__.SetStruct())
