from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Disconnect:
	"""Disconnect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("disconnect", core, parent)

	def set(self, drive: str, state: bool = None) -> None:
		"""SCPI: MMEMory:NETWork:DISConnect \n
		Snippet: driver.massMemory.network.disconnect.set(drive = '1', state = False) \n
		This command disconnects a network drive. \n
			:param drive: String containing the drive name.
			:param state: 1 | 0 | ON | OFF Optional: determines whether disconnection is forced or not 1 | ON Disconnection is forced. 0 | OFF Disconnect only if not in use.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('drive', drive, DataType.String), ArgSingle('state', state, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'MMEMory:NETWork:DISConnect {param}'.rstrip())

	# noinspection PyTypeChecker
	class DisconnectStruct(StructBase):
		"""Response structure. Fields: \n
			- Drive: str: String containing the drive name.
			- State: bool: 1 | 0 | ON | OFF Optional: determines whether disconnection is forced or not 1 | ON Disconnection is forced. 0 | OFF Disconnect only if not in use."""
		__meta_args_list = [
			ArgStruct.scalar_str('Drive'),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Drive: str = None
			self.State: bool = None

	def get(self) -> DisconnectStruct:
		"""SCPI: MMEMory:NETWork:DISConnect \n
		Snippet: value: DisconnectStruct = driver.massMemory.network.disconnect.get() \n
		This command disconnects a network drive. \n
			:return: structure: for return value, see the help for DisconnectStruct structure arguments."""
		return self._core.io.query_struct(f'MMEMory:NETWork:DISConnect?', self.__class__.DisconnectStruct())
