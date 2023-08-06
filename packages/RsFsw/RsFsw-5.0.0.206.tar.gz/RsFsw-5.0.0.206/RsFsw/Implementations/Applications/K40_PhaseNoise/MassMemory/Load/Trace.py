from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, trace: float, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: MMEMory:LOAD<n>:TRACe \n
		Snippet: driver.applications.k40PhaseNoise.massMemory.load.trace.set(trace = 1.0, filename = '1', window = repcap.Window.Default) \n
		This command imports trace data from the specified window to an ASCII file. For details on the file format see
		'Reference: ASCII File Export Format'. \n
			:param trace: Number of the trace to be stored (This parameter is ignored for method RsFsw.FormatPy.Dimport.Traces.set ALL) .
			:param filename: String containing the path and name of the import file.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Load')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('trace', trace, DataType.Float), ArgSingle('filename', filename, DataType.String))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'MMEMory:LOAD{window_cmd_val}:TRACe {param}'.rstrip())

	# noinspection PyTypeChecker
	class TraceStruct(StructBase):
		"""Response structure. Fields: \n
			- Trace: float: Number of the trace to be stored (This parameter is ignored for [CMDLINK: FORMat:DIMPort:TRACes CMDLINK] ALL) .
			- Filename: str: String containing the path and name of the import file."""
		__meta_args_list = [
			ArgStruct.scalar_float('Trace'),
			ArgStruct.scalar_str('Filename')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Trace: float = None
			self.Filename: str = None

	def get(self, window=repcap.Window.Default) -> TraceStruct:
		"""SCPI: MMEMory:LOAD<n>:TRACe \n
		Snippet: value: TraceStruct = driver.applications.k40PhaseNoise.massMemory.load.trace.get(window = repcap.Window.Default) \n
		This command imports trace data from the specified window to an ASCII file. For details on the file format see
		'Reference: ASCII File Export Format'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Load')
			:return: structure: for return value, see the help for TraceStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'MMEMory:LOAD{window_cmd_val}:TRACe?', self.__class__.TraceStruct())
