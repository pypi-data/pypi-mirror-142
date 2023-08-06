from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Copy:
	"""Copy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("copy", core, parent)

	def set(self, arg_0: enums.TraceTypeNumeric, arg_1: enums.TraceTypeNumeric, window=repcap.Window.Default) -> None:
		"""SCPI: TRACe<n>:COPY \n
		Snippet: driver.applications.k14Xnr5G.trace.copy.set(arg_0 = enums.TraceTypeNumeric.TRACe1, arg_1 = enums.TraceTypeNumeric.TRACe1, window = repcap.Window.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param arg_1: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Enum, enums.TraceTypeNumeric), ArgSingle('arg_1', arg_1, DataType.Enum, enums.TraceTypeNumeric))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'TRACe{window_cmd_val}:COPY {param}'.rstrip())

	# noinspection PyTypeChecker
	class CopyStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: enums.TraceTypeNumeric: No parameter help available
			- Arg_1: enums.TraceTypeNumeric: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Arg_0', enums.TraceTypeNumeric),
			ArgStruct.scalar_enum('Arg_1', enums.TraceTypeNumeric)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: enums.TraceTypeNumeric = None
			self.Arg_1: enums.TraceTypeNumeric = None

	def get(self, window=repcap.Window.Default) -> CopyStruct:
		"""SCPI: TRACe<n>:COPY \n
		Snippet: value: CopyStruct = driver.applications.k14Xnr5G.trace.copy.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: structure: for return value, see the help for CopyStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'TRACe{window_cmd_val}:COPY?', self.__class__.CopyStruct())
