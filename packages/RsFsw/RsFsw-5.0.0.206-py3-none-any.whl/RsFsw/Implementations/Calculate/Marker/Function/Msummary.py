from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msummary:
	"""Msummary commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msummary", core, parent)

	def set(self, time_offset: float, meas_time: float, pulse_period: float, of_pulses: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:MSUMmary \n
		Snippet: driver.calculate.marker.function.msummary.set(time_offset = 1.0, meas_time = 1.0, pulse_period = 1.0, of_pulses = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command configures power measurements on pulses in the time domain. To evaluate the pulse power, the R&S FSW uses
		the data captured during a previous measurement. The data recorded during the set measurement time is combined to a
		measured value for each pulse according to the detector specified and the indicated number of results is output as a list.
		To get a valid result, you have to perform a complete measurement with synchronization to the end of the measurement
		before reading out the result. This is only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.
		Initiate.Continuous.set. \n
			:param time_offset: Defines a time offset to start the measurement at the first pulse of a trace. Unit: s
			:param meas_time: Defines the measurement time. Unit: s
			:param pulse_period: Defines the pulse period. Unit: s
			:param of_pulses: Defines the number of pulses to measure.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('time_offset', time_offset, DataType.Float), ArgSingle('meas_time', meas_time, DataType.Float), ArgSingle('pulse_period', pulse_period, DataType.Float), ArgSingle('of_pulses', of_pulses, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:MSUMmary {param}'.rstrip())

	# noinspection PyTypeChecker
	class MsummaryStruct(StructBase):
		"""Response structure. Fields: \n
			- Time_Offset: float: Defines a time offset to start the measurement at the first pulse of a trace. Unit: s
			- Meas_Time: float: Defines the measurement time. Unit: s
			- Pulse_Period: float: Defines the pulse period. Unit: s
			- Of_Pulses: float: Defines the number of pulses to measure."""
		__meta_args_list = [
			ArgStruct.scalar_float('Time_Offset'),
			ArgStruct.scalar_float('Meas_Time'),
			ArgStruct.scalar_float('Pulse_Period'),
			ArgStruct.scalar_float('Of_Pulses')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Time_Offset: float = None
			self.Meas_Time: float = None
			self.Pulse_Period: float = None
			self.Of_Pulses: float = None

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> MsummaryStruct:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:MSUMmary \n
		Snippet: value: MsummaryStruct = driver.calculate.marker.function.msummary.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command configures power measurements on pulses in the time domain. To evaluate the pulse power, the R&S FSW uses
		the data captured during a previous measurement. The data recorded during the set measurement time is combined to a
		measured value for each pulse according to the detector specified and the indicated number of results is output as a list.
		To get a valid result, you have to perform a complete measurement with synchronization to the end of the measurement
		before reading out the result. This is only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.
		Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: structure: for return value, see the help for MsummaryStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:MSUMmary?', self.__class__.MsummaryStruct())
