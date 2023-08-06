from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- System_Messages: str: String containing all messages in the 'System Messages' table.
			- Remote_Errors: str: Error_no| Description| Command| Date| Time Comma-separated list of errors from the 'Remote Errors' table, where: Error_no: device-specific error code Description: brief description of the error Command: remote command causing the error Date|Time: date and time the error occurred"""
		__meta_args_list = [
			ArgStruct.scalar_str('System_Messages'),
			ArgStruct.scalar_raw_str('Remote_Errors')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.System_Messages: str = None
			self.Remote_Errors: str = None

	def get(self, mess_type: enums.MessageType = None) -> GetStruct:
		"""SCPI: SYSTem:ERRor:LIST \n
		Snippet: value: GetStruct = driver.system.error.listPy.get(mess_type = enums.MessageType.REMote) \n
		This command queries the error messages that occur during R&S FSW operation. \n
			:param mess_type: SMSG | REMote SMSG (default) Queries the system messages which occurred during manual operation. REMote Queries the error messages that occurred during remote operation. Note: The remote error list is automatically cleared when the R&S FSW is shut down.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mess_type', mess_type, DataType.Enum, enums.MessageType, is_optional=True))
		return self._core.io.query_struct(f'SYSTem:ERRor:LIST? {param}'.rstrip(), self.__class__.GetStruct())
