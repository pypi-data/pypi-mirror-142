from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.Utilities import trim_str_response
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Memory:
	"""Memory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("memory", core, parent)

	def get(self, offset_samples: int = None, no_of_samples: int = None) -> str:
		"""SCPI: TRACe:IQ:DATA:MEMory \n
		Snippet: value: str = driver.applications.k60Transient.trace.iq.data.memory.get(offset_samples = 1, no_of_samples = 1) \n
		This command queries the I/Q data currently stored in the capture buffer of the R&S FSW. By default, the command returns
		all I/Q data in the memory. You can, however, narrow down the amount of data that the command returns using the optional
		parameters. If no parameters are specified with the command, the entire trace data is retrieved; in this case, the
		command returns the same results as method RsFsw.Trace.Iq.Data.get_. (Note, however, that the method RsFsw.Trace.Iq.Data.
		get_ command initiates a new measurement before returning the captured values, rather than returning the existing data in
		the memory.) This command is not available for traces captured with the optional 2 GHz/ 5 GHz bandwidth extension (R&S
		FSW-B2000/B5000) . The command returns a comma-separated list of the measured values in floating point format
		(comma-separated values = CSV) . The number of values returned is 2 * the number of complex samples. The total number of
		complex samples is displayed in the channel bar in manual operation and can be calculated as: <SampleRate> *
		<CaptureTime> \n
			:param offset_samples: Selects an offset at which the output of data should start in relation to the first data. If omitted, all captured samples are output, starting with the first sample. Range: 0 to # of samples – 1, with # of samples being the maximum number of captured values
			:param no_of_samples: Number of samples you want to query, beginning at the offset you have defined. If omitted, all captured samples (starting at offset) are output. Range: 1 to # of samples - offset samples with # of samples maximum number of captured values
			:return: iq_data: Measured value pair (I,Q) for each sample that has been recorded. By default, the first half of the list contains the I values, the second half the Q values. The order can be configured using method RsFsw.Applications.K18_AmplifierEt.Trace.Iq.Data.FormatPy.set. The data format of the individual values depends on method RsFsw.FormatPy.Data.set. Unit: V"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('offset_samples', offset_samples, DataType.Integer, None, is_optional=True), ArgSingle('no_of_samples', no_of_samples, DataType.Integer, None, is_optional=True))
		response = self._core.io.query_str(f'TRACe:IQ:DATA:MEMory? {param}'.rstrip())
		return trim_str_response(response)
