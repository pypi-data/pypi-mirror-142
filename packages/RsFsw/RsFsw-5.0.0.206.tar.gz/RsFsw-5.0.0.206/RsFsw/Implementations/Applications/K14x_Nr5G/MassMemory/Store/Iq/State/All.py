from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, arg_0: int, arg_1: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe:ALL \n
		Snippet: driver.applications.k14Xnr5G.massMemory.store.iq.state.all.set(arg_0 = 1, arg_1 = '1', store = repcap.Store.Default) \n
		This command writes the captured I/Q data of all measurements in a combined measurement sequence to a file.
		The file extension is *.iq.tar. By default, the contents of the file are in 32-bit floating point format. \n
			:param arg_0: No help available
			:param arg_1: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Integer), ArgSingle('arg_1', arg_1, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:STATe:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: int: No parameter help available
			- Arg_1: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Arg_0'),
			ArgStruct.scalar_str('Arg_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: int = None
			self.Arg_1: str = None

	def get(self, store=repcap.Store.Default) -> AllStruct:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe:ALL \n
		Snippet: value: AllStruct = driver.applications.k14Xnr5G.massMemory.store.iq.state.all.get(store = repcap.Store.Default) \n
		This command writes the captured I/Q data of all measurements in a combined measurement sequence to a file.
		The file extension is *.iq.tar. By default, the contents of the file are in 32-bit floating point format. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		return self._core.io.query_struct(f'MMEMory:STORe{store_cmd_val}:IQ:STATe:ALL?', self.__class__.AllStruct())
