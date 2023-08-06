from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Memory:
	"""Memory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("memory", core, parent)

	def get(self, points_offset: int, points_count: int) -> List[float]:
		"""SCPI: TRACe:IQ:DATA:MEMory \n
		Snippet: value: List[float] = driver.trace.iq.data.memory.get(points_offset = 1, points_count = 1) \n
		This command queries the I/Q data currently stored in the capture buffer of the R&S FSW. By default, the command returns
		all I/Q data in the memory. You can, however, narrow down the amount of data that the command returns using the optional
		parameters. If no parameters are specified with the command, the entire trace data is retrieved; in this case, the
		command returns the same results as method RsFsw.Trace.Iq.Data.get_. (Note, however, that the method RsFsw.Trace.Iq.Data.
		get_ command initiates a new measurement before returning the captured values, rather than returning the existing data in
		the memory.) This command is not available for traces captured with the optional 2 GHz / 5 GHz bandwidth extension (R&S
		FSW-B2000/B5000) . The command returns a comma-separated list of the measured values in floating point format
		(comma-separated values = CSV) . The number of values returned is 2 * the number of complex samples. The total number of
		complex samples is displayed in the channel bar in manual operation and can be calculated as: <SampleRate> *
		<CaptureTime> (See TRACe:IQ:SET, method RsFsw.Applications.K10x_Lte.Trace.Iq.SymbolRate.get_ and [SENSe:]SWEep:TIME) \n
			:param points_offset: No help available
			:param points_count: No help available
			:return: iq_data: Measured value pair (I,Q) for each sample that has been recorded. By default, the first half of the list contains the I values, the second half the Q values. The order can be configured using method RsFsw.Applications.K18_AmplifierEt.Trace.Iq.Data.FormatPy.set. The data format of the individual values depends on method RsFsw.FormatPy.Data.set. Unit: V"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('points_offset', points_offset, DataType.Integer), ArgSingle('points_count', points_count, DataType.Integer))
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe:IQ:DATA:MEMory? {param}'.rstrip())
		return response
