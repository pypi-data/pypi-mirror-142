from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transducer:
	"""Transducer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transducer", core, parent)

	def set(self, transducer: str, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:TRANsducer \n
		Snippet: driver.sense.listPy.range.transducer.set(transducer = '1', rangePy = repcap.RangePy.Default) \n
		This command selects a transducer factor for a spurious emission measurement range.
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- The transducer must cover at least the span of the range.
			- The x-axis has to be linear.
			- The unit has to be dB.
		The sweep list cannot be configured using remote commands during an on-going sweep operation. \n
			:param transducer: String containing the transducer file name. Do not include a file extension or the file path. The file must be located in the C:/R_S/INSTR/trd directory.
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.value_to_quoted_str(transducer)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:TRANsducer {param}')

	def get(self, rangePy=repcap.RangePy.Default) -> str:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:TRANsducer \n
		Snippet: value: str = driver.sense.listPy.range.transducer.get(rangePy = repcap.RangePy.Default) \n
		This command selects a transducer factor for a spurious emission measurement range.
			INTRO_CMD_HELP: Note the following prerequisites for the selected transducer: \n
			- The transducer must cover at least the span of the range.
			- The x-axis has to be linear.
			- The unit has to be dB.
		The sweep list cannot be configured using remote commands during an on-going sweep operation. \n
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: transducer: String containing the transducer file name. Do not include a file extension or the file path. The file must be located in the C:/R_S/INSTR/trd directory."""
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:LIST:RANGe{rangePy_cmd_val}:TRANsducer?')
		return trim_str_response(response)
