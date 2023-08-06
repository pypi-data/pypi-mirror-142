from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Frequency: float: Defines the pulse frequency. Range: 0 to Fmax, Unit: Hz
			- Rbw: float: Defines the resolution bandwidth. Unit: HZ
			- Meas_Time: float: Defines the measurement time. Range: 1 µs to 30 s, Unit: S
			- Trigger_Source: enums.TriggerSourceMpower: EXTernal | EXT2 | EXT3 | VIDeo Selects a trigger source. For more information see 'Configuring triggered and gated measurements'.
			- Trigger_Level: float: Defines a trigger level. The trigger level is available for the video trigger. In that case, the level is a percentage of the diagram height. In case of an external trigger, the R&S FSW uses a fix TTL level. Range: 0 to 100, Unit: PCT
			- Trigger_Offset: float: Defines the trigger delay. Range: 0 s to 30 s, Unit: s
			- Detector: enums.MpowerDetector: Selects the detector and therefore the way the measurement is evaluated. MEAN Calculates the RMS pulse power. PEAK Calculates the peak pulse power.
			- Of_Pulses: float: Defines the number of pulses included in the measurement. Range: 1 to 32001"""
		__meta_args_list = [
			ArgStruct.scalar_float('Frequency'),
			ArgStruct.scalar_float('Rbw'),
			ArgStruct.scalar_float('Meas_Time'),
			ArgStruct.scalar_enum('Trigger_Source', enums.TriggerSourceMpower),
			ArgStruct.scalar_float('Trigger_Level'),
			ArgStruct.scalar_float('Trigger_Offset'),
			ArgStruct.scalar_enum('Detector', enums.MpowerDetector),
			ArgStruct.scalar_float('Of_Pulses')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: float = None
			self.Rbw: float = None
			self.Meas_Time: float = None
			self.Trigger_Source: enums.TriggerSourceMpower = None
			self.Trigger_Level: float = None
			self.Trigger_Offset: float = None
			self.Detector: enums.MpowerDetector = None
			self.Of_Pulses: float = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: [SENSe]:MPOWer[:SEQuence] \n
		Snippet with structure: \n
		structure = driver.sense.mpower.sequence.SetStruct() \n
		structure.Frequency: float = 1.0 \n
		structure.Rbw: float = 1.0 \n
		structure.Meas_Time: float = 1.0 \n
		structure.Trigger_Source: enums.TriggerSourceMpower = enums.TriggerSourceMpower.EXT2 \n
		structure.Trigger_Level: float = 1.0 \n
		structure.Trigger_Offset: float = 1.0 \n
		structure.Detector: enums.MpowerDetector = enums.MpowerDetector.MEAN \n
		structure.Of_Pulses: float = 1.0 \n
		driver.sense.mpower.sequence.set(structure) \n
		This command configures and initiates the pulse power measurement. The R&S FSW caches all measurement parameters that you
		can set with this command. If you use the command repeatedly, the R&S FSW only changes those settings that you have
		actually changed before initiating the measurement. Thus, measurement times are kept as low as possible.
		If you synchronize the measurement with *OPC, the R&S FSW produces a service request when all frequencies have been
		measured and the number of individual measurements has been performed. Note that using the command as a query initiates
		the measurement and returns the results if all frequencies have been measured. For more information on querying the
		results see [SENSe:]LIST:POWer:RESult?. \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'SENSe:MPOWer:SEQuence', structure)

	def get(self) -> List[float]:
		"""SCPI: [SENSe]:MPOWer[:SEQuence] \n
		Snippet: value: List[float] = driver.sense.mpower.sequence.get() \n
		This command configures and initiates the pulse power measurement. The R&S FSW caches all measurement parameters that you
		can set with this command. If you use the command repeatedly, the R&S FSW only changes those settings that you have
		actually changed before initiating the measurement. Thus, measurement times are kept as low as possible.
		If you synchronize the measurement with *OPC, the R&S FSW produces a service request when all frequencies have been
		measured and the number of individual measurements has been performed. Note that using the command as a query initiates
		the measurement and returns the results if all frequencies have been measured. For more information on querying the
		results see [SENSe:]LIST:POWer:RESult?. \n
			:return: power_levels: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list(f'SENSe:MPOWer:SEQuence?')
		return response
