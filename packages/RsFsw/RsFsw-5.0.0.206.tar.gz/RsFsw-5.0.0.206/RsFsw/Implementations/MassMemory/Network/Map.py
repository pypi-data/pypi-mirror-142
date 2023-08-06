from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Map:
	"""Map commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("map", core, parent)

	def set(self, file_path: str, ip: str, user_name: str = None, password: str = None, state: bool = None) -> None:
		"""SCPI: MMEMory:NETWork:MAP \n
		Snippet: driver.massMemory.network.map.set(file_path = '1', ip = '1', user_name = '1', password = '1', state = False) \n
		This command maps a drive to a server or server directory of the network. Note that you have to allow sharing for a
		server or folder in Microsoft networks first. \n
			:param file_path: String containing the drive name or path of the directory you want to map.
			:param ip: String containing the host name of the computer or the IP address and the share name of the drive. '/host name or IP address/share name'
			:param user_name: String containing a user name in the network. The user name is optional.
			:param password: String containing the password corresponding to the UserName. The password is optional.
			:param state: ON | OFF | 1 | 0 ON | 1 Reconnects at logon with the same user name. OFF | 0 Does not reconnect at logon.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('file_path', file_path, DataType.String), ArgSingle('ip', ip, DataType.String), ArgSingle('user_name', user_name, DataType.String, None, is_optional=True), ArgSingle('password', password, DataType.String, None, is_optional=True), ArgSingle('state', state, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'MMEMory:NETWork:MAP {param}'.rstrip())

	# noinspection PyTypeChecker
	class MapStruct(StructBase):
		"""Response structure. Fields: \n
			- File_Path: str: String containing the drive name or path of the directory you want to map.
			- Ip: str: String containing the host name of the computer or the IP address and the share name of the drive. '/host name or IP address/share name'
			- User_Name: str: String containing a user name in the network. The user name is optional.
			- Password: str: String containing the password corresponding to the UserName. The password is optional.
			- State: bool: ON | OFF | 1 | 0 ON | 1 Reconnects at logon with the same user name. OFF | 0 Does not reconnect at logon."""
		__meta_args_list = [
			ArgStruct.scalar_str('File_Path'),
			ArgStruct.scalar_str('Ip'),
			ArgStruct.scalar_str('User_Name'),
			ArgStruct.scalar_str('Password'),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.File_Path: str = None
			self.Ip: str = None
			self.User_Name: str = None
			self.Password: str = None
			self.State: bool = None

	def get(self) -> MapStruct:
		"""SCPI: MMEMory:NETWork:MAP \n
		Snippet: value: MapStruct = driver.massMemory.network.map.get() \n
		This command maps a drive to a server or server directory of the network. Note that you have to allow sharing for a
		server or folder in Microsoft networks first. \n
			:return: structure: for return value, see the help for MapStruct structure arguments."""
		return self._core.io.query_struct(f'MMEMory:NETWork:MAP?', self.__class__.MapStruct())
