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
		Snippet: driver.applications.k18AmplifierEt.massMemory.store.trace.set(trace = 1, filename = '1', store = repcap.Store.Default) \n
		This command exports trace data to a file. \n
			:param trace: Number of the trace you want to save. Note that the available number of traces depends on the selected result display. The value '0' exports all traces in a window. To export all traces in all windows, turn on the feature to export all traces and all results first (method RsFsw.Applications.K10x_Lte.FormatPy.Dexport.Traces.set) . The suffix at STORen and the trace id, Trace, are ignored in that case. Range: 0 to 6
			:param filename: String containing the path and file name.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('trace', trace, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:TRACe {param}'.rstrip())
