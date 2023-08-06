from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: int, filename: str) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.applications.k91Wlan.massMemory.load.iq.state.set(state = 1, filename = '1') \n
		This command restores I/Q data from a file. The file extension is *.iqw. \n
			:param state: No help available
			:param filename: string String containing the path and name of the source file.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		self._core.io.write(f'MMEMory:LOAD:IQ:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- State: int: No parameter help available
			- Filename: str: string String containing the path and name of the source file."""
		__meta_args_list = [
			ArgStruct.scalar_int('State'),
			ArgStruct.scalar_str('Filename')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: int = None
			self.Filename: str = None

	def get(self) -> StateStruct:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: value: StateStruct = driver.applications.k91Wlan.massMemory.load.iq.state.get() \n
		This command restores I/Q data from a file. The file extension is *.iqw. \n
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		return self._core.io.query_struct(f'MMEMory:LOAD:IQ:STATe?', self.__class__.StateStruct())
