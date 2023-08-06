from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, position: float, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:TRACe \n
		Snippet: driver.applications.k70Vsa.massMemory.store.iq.trace.set(position = 1.0, filename = '1', store = repcap.Store.Default) \n
		Stores the I/Q data for the displayed trace in the selected window to a file in iq.tar format. This command is only
		available for result types that provide I/Q data based on the error vector, such as the Vector I/Q or Real/Imag displays. \n
			:param position: 1..n Window
			:param filename: String containing the path and name of the target file.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('position', position, DataType.Float), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:TRACe {param}'.rstrip())
