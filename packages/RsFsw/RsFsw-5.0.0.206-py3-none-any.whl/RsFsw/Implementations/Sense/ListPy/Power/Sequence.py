from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	# noinspection PyTypeChecker
	class SequenceStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Frequency: List[float]: Defines the frequency. Each frequency corresponds to one list entry. Range: 0 to Fmax, Unit: Hz
			- Ref_Level: List[float]: Defines the reference level for a list entry. Range: -130 to 30, Unit: dBm
			- Rfattenuation: List[float]: Defines the RF attenuation for a list entry. Range: 0 to 70, Unit: dB
			- Filter_Type: List[float or bool]: Selects the filter type for a list entry. For more information see [SENSe:]BANDwidth[:RESolution]:TYPE.
			- Rbw: List[enums.FilterTypeK91]: Defines the resolution bandwidth for a list entry.
			- Vbw: List[float]: Defines the measurement time for a list entry.
			- Meas_Time: List[float]: Defines the measurement time for a list entry. Range: 1 µs to 16000 s, Unit: s
			- Trigger_Level: List[float]: Reserved for future use; currently: must be 0.
			- Power_Level: List[float]: numeric value Defines the electronic attenuation for a list entry. A setting other than 0 (OFF) requires option R&S FSW-B25. Range: 0 to 30, Unit: dB"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Ref_Level', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rfattenuation', DataType.FloatList, None, False, True, 1),
			ArgStruct('Filter_Type', DataType.FloatList, None, False, True, 1),
			ArgStruct('Rbw', DataType.EnumList, enums.FilterTypeK91, False, True, 1),
			ArgStruct('Vbw', DataType.FloatList, None, False, True, 1),
			ArgStruct('Meas_Time', DataType.FloatList, None, False, True, 1),
			ArgStruct('Trigger_Level', DataType.FloatList, None, False, True, 1),
			ArgStruct('Power_Level', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Ref_Level: List[float] = None
			self.Rfattenuation: List[float] = None
			self.Filter_Type: List[float or bool] = None
			self.Rbw: List[enums.FilterTypeK91] = None
			self.Vbw: List[float] = None
			self.Meas_Time: List[float] = None
			self.Trigger_Level: List[float] = None
			self.Power_Level: List[float] = None

	def set(self, structure: SequenceStruct) -> None:
		"""SCPI: [SENSe]:LIST:POWer[:SEQuence] \n
		Snippet with structure: \n
		structure = driver.sense.listPy.power.sequence.SequenceStruct() \n
		structure.Frequency: List[float] = [1.1, 2.2, 3.3] \n
		structure.Ref_Level: List[float] = [1.1, 2.2, 3.3] \n
		structure.Rfattenuation: List[float] = [1.1, 2.2, 3.3] \n
		structure.Filter_Type: List[float or bool] = [1.1, True, 2.2, False, 3.3] \n
		structure.Rbw: List[enums.FilterTypeK91] = [FilterTypeK91.CFILter, FilterTypeK91.RRC] \n
		structure.Vbw: List[float] = [1.1, 2.2, 3.3] \n
		structure.Meas_Time: List[float] = [1.1, 2.2, 3.3] \n
		structure.Trigger_Level: List[float] = [1.1, 2.2, 3.3] \n
		structure.Power_Level: List[float] = [1.1, 2.2, 3.3] \n
		driver.sense.listPy.power.sequence.set(structure) \n
		This command configures and initiates the List Evaluation measurement. The list can contain up to 200 entries
		(frequencies) . You can define a different instrument setup for each frequency that is in the list. If you synchronize
		the measurement with *OPC, the R&S FSW produces a service request when all frequencies have been measured and the number
		of individual measurements has been performed. Note that using the command as a query initiates the measurement and
		returns the results if all frequencies have been measured. For more information on querying the results see
		[SENSe:]LIST:POWer:RESult?. \n
			:param structure: for set value, see the help for SequenceStruct structure arguments.
		"""
		self._core.io.write_struct(f'SENSe:LIST:POWer:SEQuence', structure)

	def get(self) -> SequenceStruct:
		"""SCPI: [SENSe]:LIST:POWer[:SEQuence] \n
		Snippet: value: SequenceStruct = driver.sense.listPy.power.sequence.get() \n
		This command configures and initiates the List Evaluation measurement. The list can contain up to 200 entries
		(frequencies) . You can define a different instrument setup for each frequency that is in the list. If you synchronize
		the measurement with *OPC, the R&S FSW produces a service request when all frequencies have been measured and the number
		of individual measurements has been performed. Note that using the command as a query initiates the measurement and
		returns the results if all frequencies have been measured. For more information on querying the results see
		[SENSe:]LIST:POWer:RESult?. \n
			:return: structure: for return value, see the help for SequenceStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:LIST:POWer:SEQuence?', self.__class__.SequenceStruct())
