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

	def set(self, trace: float, arg_1: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:TRACe \n
		Snippet: driver.applications.k10Xlte.massMemory.store.trace.set(trace = 1.0, arg_1 = '1', store = repcap.Store.Default) \n
		This command exports trace data from the specified window to an ASCII file. Secure User Mode In secure user mode,
		settings that are stored on the instrument are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory
		limit reached' error can occur although the hard disk indicates that storage space is still available. To store data
		permanently, select an external storage location such as a USB memory device. For details, see 'Protecting Data Using the
		Secure User Mode'. \n
			:param trace: Number of the trace to be stored
			:param arg_1: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('trace', trace, DataType.Float), ArgSingle('arg_1', arg_1, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TRACe {param}'.rstrip())

	# noinspection PyTypeChecker
	class TraceStruct(StructBase):
		"""Response structure. Fields: \n
			- Trace: float: Number of the trace to be stored
			- Arg_1: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Trace'),
			ArgStruct.scalar_str('Arg_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Trace: float = None
			self.Arg_1: str = None

	def get(self, store=repcap.Store.Default) -> TraceStruct:
		"""SCPI: MMEMory:STORe<n>:TRACe \n
		Snippet: value: TraceStruct = driver.applications.k10Xlte.massMemory.store.trace.get(store = repcap.Store.Default) \n
		This command exports trace data from the specified window to an ASCII file. Secure User Mode In secure user mode,
		settings that are stored on the instrument are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory
		limit reached' error can occur although the hard disk indicates that storage space is still available. To store data
		permanently, select an external storage location such as a USB memory device. For details, see 'Protecting Data Using the
		Secure User Mode'. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: structure: for return value, see the help for TraceStruct structure arguments."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		return self._core.io.query_struct(f'MMEMory:STORe{store_cmd_val}:TRACe?', self.__class__.TraceStruct())
