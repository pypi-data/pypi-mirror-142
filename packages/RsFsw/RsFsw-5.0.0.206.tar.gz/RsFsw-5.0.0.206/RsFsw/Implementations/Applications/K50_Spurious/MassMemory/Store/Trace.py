from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, trace: int, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:TRACe \n
		Snippet: driver.applications.k50Spurious.massMemory.store.trace.set(trace = 1, filename = '1', store = repcap.Store.Default) \n
		This command exports trace data from the specified window to an ASCII file. Secure User Mode In secure user mode,
		settings that are stored on the instrument are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory
		limit reached' error can occur although the hard disk indicates that storage space is still available. To store data
		permanently, select an external storage location such as a USB memory device. For details, see 'Protecting Data Using the
		Secure User Mode'. \n
			:param trace: Number of the trace to be stored
			:param filename: String containing the path and name of the target file.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('trace', trace, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TRACe {param}'.rstrip())
