from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, position: int, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe \n
		Snippet: driver.applications.k91Wlan.massMemory.store.iq.state.set(position = 1, filename = '1', store = repcap.Store.Default) \n
		This command writes the captured I/Q data to a file. The file extension is *.iq.tar. By default, the contents of the file
		are in 32-bit floating point format. \n
			:param position: 1..n
			:param filename: String containing the path and name of the target file.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('position', position, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Position: int: No parameter help available
			- Filename: str: String containing the path and name of the target file."""
		__meta_args_list = [
			ArgStruct.scalar_int('Position'),
			ArgStruct.scalar_str('Filename')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Position: int = None
			self.Filename: str = None

	def get(self, store=repcap.Store.Default) -> StateStruct:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe \n
		Snippet: value: StateStruct = driver.applications.k91Wlan.massMemory.store.iq.state.get(store = repcap.Store.Default) \n
		This command writes the captured I/Q data to a file. The file extension is *.iq.tar. By default, the contents of the file
		are in 32-bit floating point format. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		return self._core.io.query_struct(f'MMEMory:STORe{store_cmd_val}:IQ:STATe?', self.__class__.StateStruct())
