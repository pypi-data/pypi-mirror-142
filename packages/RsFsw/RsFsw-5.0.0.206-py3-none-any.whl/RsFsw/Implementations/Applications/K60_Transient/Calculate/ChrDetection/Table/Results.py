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
			- Idn: str: char_data Timestamp which corresponds to the absolute time the beginning of the chirp was detected
			- Chirp_No: float: Consecutive number of detected chirp, starts at 1 for each new measurement
			- State_Index: float: Consecutive number of corresponding nominal chirp state as defined in the 'Chirp States' table (see [CMDLINK: CALCulaten:CHRDetection:STATes[:DATA] CMDLINK])
			- Begin: str: char_data Time offset from the analysis region start at which the signal first enters the tolerance area of a nominal chirp Unit: ms
			- Length: str: char_data The duration of a chirp from begin to end, that is, the time the signal remains in the tolerance area of a nominal chirp. Unit: ms
			- Crate: str: char_data Derivative of the FM vs time trace within the frequency measurement range Unit: kHz/μs
			- Crate_Dev: float: Deviation of the detected chirp rate from the nominal chirp state (in kHz/us) . For details see 'Chirp State Deviation'. Unit: kHz/μs
			- Freq_Avg: float: Average frequency measured within the frequency measurement range of the chirp Unit: kHz
			- Fm_Dev_Max: float: Maximum deviation of the chirp frequency from the nominal chirp frequency as defined in the 'Chirp States' table. The deviation is calculated within the frequency measurement range of the chirp. For details see 'Frequency Deviation (Peak) '. Unit: kHz
			- Fm_Dev_Rms: float: RMS deviation of the chirp frequency from the nominal (linear) chirp frequency as defined in the 'Chirp States' table. The deviation is calculated within the frequency measurement range of the chirp. For details see 'Frequency Deviation (RMS) '. Unit: kHz
			- Fm_Dev_Avg: float: Average deviation of the chirp frequency from the nominal (linear) chirp frequency as defined in the 'Chirp States' table. The deviation is calculated within the frequency measurement range of the chirp. For details see 'Frequency Deviation (Average) '. Unit: kHz
			- Pm_Dev_Max: float: Maximum deviation of the chirp phase from the nominal chirp phase as defined in the 'Chirp States' table. The deviation is calculated within the frequency measurement range of the chirp. For details see 'Phase Deviation (Peak) '. Unit: kHz
			- Pm_Dev_Rms: float: RMS deviation of the chirp phase from the nominal (linear) chirp phase as defined in the 'Chirp States' table. The deviation is calculated within the frequency measurement range of the chirp. For details see 'Phase Deviation (RMS) '. Unit: kHz
			- Pm_Dev_Avg: float: Average deviation of the chirp phase from the nominal (linear) chirp phase as defined in the 'Chirp States' table. The deviation is calculated within the frequency measurement range of the chirp. For details see 'Phase Deviation (Average) '. Unit: kHz
			- Pow_Min: float: Minimum power level measured during a chirp. Which part of the chirp precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm
			- Pow_Max: float: Maximum power level measured during a chirp. Which part of the chirp precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm
			- Pow_Avg: float: Average power level measured during a chirp. Which part of the chirp precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm
			- Pow_Rip: float: Power level measured during the chirp ripple time. Which part of the chirp precisely is used for calculation depends on the power parameters in the 'Power' measurement range configuration. Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Idn'),
			ArgStruct.scalar_float('Chirp_No'),
			ArgStruct.scalar_float('State_Index'),
			ArgStruct.scalar_raw_str('Begin'),
			ArgStruct.scalar_raw_str('Length'),
			ArgStruct.scalar_raw_str('Crate'),
			ArgStruct.scalar_float('Crate_Dev'),
			ArgStruct.scalar_float('Freq_Avg'),
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
			self.Chirp_No: float = None
			self.State_Index: float = None
			self.Begin: str = None
			self.Length: str = None
			self.Crate: str = None
			self.Crate_Dev: float = None
			self.Freq_Avg: float = None
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
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:RESults \n
		Snippet: value: GetStruct = driver.applications.k60Transient.calculate.chrDetection.table.results.get(start = 1, end = 1, window = repcap.Window.Default) \n
		This command queries the chirp results table. The result is a comma-separated list of value sets, one set for each chirp.
		If no query parameters are specified, the results for all detected chirps are returned. Which values are returned depends
		on the enabled parameters for the results tables (see method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.
		Table.Column.set) . \n
			:param start: integer The chirp number of the first chirp to be returned. Chirp numbers start at 1.
			:param end: integer The chirp number of the last chirp to be returned.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('start', start, DataType.Integer, None, is_optional=True), ArgSingle('end', end, DataType.Integer, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:RESults? {param}'.rstrip(), self.__class__.GetStruct())
