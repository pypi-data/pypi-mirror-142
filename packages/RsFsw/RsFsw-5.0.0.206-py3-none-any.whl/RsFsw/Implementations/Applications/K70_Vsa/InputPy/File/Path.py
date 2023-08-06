from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, iq_filename: str, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:FILE:PATH \n
		Snippet: driver.applications.k70Vsa.inputPy.file.path.set(iq_filename = '1', inputIx = repcap.InputIx.Default) \n
		This command selects the I/Q data file to be used as input for further measurements.
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- .iq.tar
			- .iqw
			- .csv
			- .mat
			- .wv
			- .aid
		Only a single data stream or channel can be used as input, even if multiple streams or channels are stored in the file.
		For some file formats that do not provide the sample rate and measurement time or record length, you must define these
		parameters manually. Otherwise the traces are not visible in the result displays. For details, see 'Basics on Input from
		I/Q Data Files'. \n
			:param iq_filename: No help available
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.value_to_quoted_str(iq_filename)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:FILE:PATH {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> str:
		"""SCPI: INPut<ip>:FILE:PATH \n
		Snippet: value: str = driver.applications.k70Vsa.inputPy.file.path.get(inputIx = repcap.InputIx.Default) \n
		This command selects the I/Q data file to be used as input for further measurements.
			INTRO_CMD_HELP: The I/Q data file must be in one of the following supported formats: \n
			- .iq.tar
			- .iqw
			- .csv
			- .mat
			- .wv
			- .aid
		Only a single data stream or channel can be used as input, even if multiple streams or channels are stored in the file.
		For some file formats that do not provide the sample rate and measurement time or record length, you must define these
		parameters manually. Otherwise the traces are not visible in the result displays. For details, see 'Basics on Input from
		I/Q Data Files'. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: iq_filename: No help available"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:FILE:PATH?')
		return trim_str_response(response)
