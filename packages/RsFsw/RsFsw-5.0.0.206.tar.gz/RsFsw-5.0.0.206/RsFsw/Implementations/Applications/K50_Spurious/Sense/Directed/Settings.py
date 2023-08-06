from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Settings:
	"""Settings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("settings", core, parent)

	def set(self, frequency: List[float] = None, search_span: List[float] = None, det_threshold: List[float] = None, desired_spur_snr: List[float] = None) -> None:
		"""SCPI: [SENSe]:DIRected:SETTings \n
		Snippet: driver.applications.k50Spurious.sense.directed.settings.set(frequency = [1.1, 2.2, 3.3], search_span = [1.1, 2.2, 3.3], det_threshold = [1.1, 2.2, 3.3], desired_spur_snr = [1.1, 2.2, 3.3]) \n
		Defines the current directed search configuration, that is: all frequency spans to be measured in detail. The current
		configuration table is overwritten. Note that all entries must be defined in one command so that the R&S FSW Spurious
		measurements application can detect any possible conflicts between the frequency spans. The parameters are defined as a
		comma-separated list with one line per span, using the following syntax: <Frequency>,<SearchSpan>,<DetThreshold>,<SNR>
		For details on the parameters see 'Directed Search Measurement settings') . \n
			:param frequency: numeric value Center frequency for directed search measurement of the spur Unit: HZ
			:param search_span: numeric value The span around the frequency for which a detailed measurement (spurious detection sweep and spot search) is performed. Note that the frequency spans must be distinct, that is: they may not overlap. Unit: HZ
			:param det_threshold: numeric value Absolute threshold that the power level must exceed for a spur to be detected. Unit: dBm
			:param desired_spur_snr: numeric value Minimum signal-to-noise ratio that the power level must exceed for a spur to be detected during the spot search Unit: dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('frequency', frequency, DataType.FloatList, None, True, True, 1), ArgSingle('search_span', search_span, DataType.FloatList, None, True, True, 1), ArgSingle('det_threshold', det_threshold, DataType.FloatList, None, True, True, 1), ArgSingle('desired_spur_snr', desired_spur_snr, DataType.FloatList, None, True, True, 1))
		self._core.io.write(f'SENSe:DIRected:SETTings {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Search_Span: List[float]: numeric value The span around the frequency for which a detailed measurement (spurious detection sweep and spot search) is performed. Note that the frequency spans must be distinct, that is: they may not overlap. Unit: HZ
			- Det_Threshold: List[float]: numeric value Absolute threshold that the power level must exceed for a spur to be detected. Unit: dBm
			- Desired_Spur_Snr: List[float]: numeric value Minimum signal-to-noise ratio that the power level must exceed for a spur to be detected during the spot search Unit: dB"""
		__meta_args_list = [
			ArgStruct('Search_Span', DataType.FloatList, None, False, True, 1),
			ArgStruct('Det_Threshold', DataType.FloatList, None, False, True, 1),
			ArgStruct('Desired_Spur_Snr', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Search_Span: List[float] = None
			self.Det_Threshold: List[float] = None
			self.Desired_Spur_Snr: List[float] = None

	def get(self) -> GetStruct:
		"""SCPI: [SENSe]:DIRected:SETTings \n
		Snippet: value: GetStruct = driver.applications.k50Spurious.sense.directed.settings.get() \n
		Defines the current directed search configuration, that is: all frequency spans to be measured in detail. The current
		configuration table is overwritten. Note that all entries must be defined in one command so that the R&S FSW Spurious
		measurements application can detect any possible conflicts between the frequency spans. The parameters are defined as a
		comma-separated list with one line per span, using the following syntax: <Frequency>,<SearchSpan>,<DetThreshold>,<SNR>
		For details on the parameters see 'Directed Search Measurement settings') . \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:DIRected:SETTings?', self.__class__.GetStruct())
