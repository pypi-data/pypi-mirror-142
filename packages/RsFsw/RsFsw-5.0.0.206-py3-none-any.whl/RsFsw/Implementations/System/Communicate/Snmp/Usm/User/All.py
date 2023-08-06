from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Count: float: Total number of registered SNMP users.
			- Name: str: List of all user names as a comma-separated list."""
		__meta_args_list = [
			ArgStruct.scalar_float('Count'),
			ArgStruct.scalar_str('Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Count: float = None
			self.Name: str = None

	def get(self) -> GetStruct:
		"""SCPI: SYSTem:COMMunicate:SNMP:USM:USER:ALL \n
		Snippet: value: GetStruct = driver.system.communicate.snmp.usm.user.all.get() \n
		This command returns the number of users and a list of all SNMP users for SNMPv3.
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- Select SNMPv3 (method RsFsw.System.Communicate.Snmp.Version.set) . \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:COMMunicate:SNMP:USM:USER:ALL?', self.__class__.GetStruct())
