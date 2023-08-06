from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Results:
	"""Results commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("results", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Idn: str: char_data timestamp which corresponds to the absolute time the beginning of the hop was detected
			- Hop_No: float: consecutive number of detected hop, starts at 1 for each new measurement
			- State_Index: float: consecutive number of corresponding nominal hop state as defined in the 'hop States' table (see [CMDLINK: CALCulaten:HOPDetection:STATes[:DATA] CMDLINK])
			- Begin: str: char_data relative time (in ms) from the capture start at which the signal first enters the tolerance area of a nominal hop (within the analysis region) Unit: ms
			- Dwell_Time: str: char_data The duration of a hop from begin to end, that is, the time the signal remains in the tolerance area of a nominal hop frequency. Unit: ms
			- Switch_Time: str: char_data The time the signal requires to 'hop' from one level to the next. It is defined as the time between a hop end and the following hop begin. Unit: ms
			- Freq_Nom: float: Nominal frequency of the hop state Unit: kHz
			- Freq_Avg: float: Average frequency measured within the frequency measurement range of the hop Unit: kHz
			- Freq_Dev: float: Deviation of the hop frequency from the nominal hop state frequency For details see 'Hop State Deviation'. Unit: kHz
			- Freq_Rel: float: Relative difference in frequency between two hops. For details see 'Relative Frequency (Hop-to-Hop) '. Unit: kHz
			- Fm_Dev_Max: float: Maximum deviation of the hop frequency from the nominal hop frequency as defined in the 'Hop States' table. The deviation is calculated within the frequency measurement range of the hop. For details see 'Frequency Deviation (Peak) '. Unit: kHz
			- Fm_Dev_Rms: float: RMS deviation of the hop frequency from the nominal (linear) hop frequency as defined in the 'Hop States' table. The deviation is calculated within the frequency measurement range of the hop. For details see 'Frequency Deviation (RMS) '. Unit: kHz
			- Fm_Dev_Avg: float: Average deviation of the hop frequency from the nominal (linear) hop frequency as defined in the 'Hop States' table. The deviation is calculated within the frequency measurement range of the hop. For details see 'Frequency Deviation (Average) '. Unit: kHz
			- Pm_Dev_Max: float: Maximum deviation of the hop phase from the nominal hop phase as defined in the 'Hop States' table. The deviation is calculated within the frequency measurement range of the hop. For details see 'Phase Deviation (Peak) '. Unit: kHz
			- Pm_Dev_Rms: float: RMS deviation of the hop phase from the nominal (linear) hop phase as defined in the 'Hop States' table. The deviation is calculated within the frequency measurement range of the hop. For details see 'Phase Deviation (RMS) '. Unit: kHz
			- Pm_Dev_Avg: float: Average deviation of the hop phase from the nominal (linear) hop phase as defined in the 'Hop States' table. The deviation is calculated within the frequency measurement range of the hop. For details see 'Phase Deviation (Average) '. Unit: kHz
			- Pow_Min: float: Minimum power level measured during a hop. Which part of the hop precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm
			- Pow_Max: float: Maximum power level measured during a hop. Which part of the hop precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm
			- Pow_Avg: float: Average power level measured during a hop. Which part of the hop precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm
			- Pow_Rip: float: Power level measured during the hop ripple time. Which part of the hop precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Idn'),
			ArgStruct.scalar_float('Hop_No'),
			ArgStruct.scalar_float('State_Index'),
			ArgStruct.scalar_raw_str('Begin'),
			ArgStruct.scalar_raw_str('Dwell_Time'),
			ArgStruct.scalar_raw_str('Switch_Time'),
			ArgStruct.scalar_float('Freq_Nom'),
			ArgStruct.scalar_float('Freq_Avg'),
			ArgStruct.scalar_float('Freq_Dev'),
			ArgStruct.scalar_float('Freq_Rel'),
			ArgStruct.scalar_float('Fm_Dev_Max'),
			ArgStruct.scalar_float('Fm_Dev_Rms'),
			ArgStruct.scalar_float('Fm_Dev_Avg'),
			ArgStruct.scalar_float('Pm_Dev_Max'),
			ArgStruct.scalar_float('Pm_Dev_Rms'),
			ArgStruct.scalar_float('Pm_Dev_Avg'),
			ArgStruct.scalar_float('Pow_Min'),
			ArgStruct.scalar_float('Pow_Max'),
			ArgStruct.scalar_float('Pow_Avg'),
			ArgStruct.scalar_float('Pow_Rip')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: str = None
			self.Hop_No: float = None
			self.State_Index: float = None
			self.Begin: str = None
			self.Dwell_Time: str = None
			self.Switch_Time: str = None
			self.Freq_Nom: float = None
			self.Freq_Avg: float = None
			self.Freq_Dev: float = None
			self.Freq_Rel: float = None
			self.Fm_Dev_Max: float = None
			self.Fm_Dev_Rms: float = None
			self.Fm_Dev_Avg: float = None
			self.Pm_Dev_Max: float = None
			self.Pm_Dev_Rms: float = None
			self.Pm_Dev_Avg: float = None
			self.Pow_Min: float = None
			self.Pow_Max: float = None
			self.Pow_Avg: float = None
			self.Pow_Rip: float = None

	def get(self, start: int = None, end: int = None, window=repcap.Window.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:RESults \n
		Snippet: value: GetStruct = driver.applications.k60Transient.calculate.hopDetection.table.results.get(start = 1, end = 1, window = repcap.Window.Default) \n
		This command queries the hop results table. The result is a comma-separated list of value sets, one set for each hop. If
		no query parameters are specified, the results for all detected hops are returned. Which values are returned depends on
		the enabled parameters for the results tables (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.
		Column.set) . \n
			:param start: integer The hop number of the first hop to be returned. Hop numbers start at 1.
			:param end: integer The hop number of the last hop to be returned.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Integer, None, is_optional=True), ArgSingle('end', end, DataType.Integer, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:RESults? {param}'.rstrip(), self.__class__.GetStruct())
