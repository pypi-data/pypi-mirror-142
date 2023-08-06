from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def set(self, name: str, access: enums.AccessType, level: enums.UserLevel, auth_pwd: str = None, priv_pwd: str = None) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:USM:USER \n
		Snippet: driver.system.communicate.snmp.usm.user.set(name = '1', access = enums.AccessType.RO, level = enums.UserLevel.AUTH, auth_pwd = '1', priv_pwd = '1') \n
		This command defines a SNMP user profile.
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- Select SNMPv3 (method RsFsw.System.Communicate.Snmp.Version.set) . \n
			:param name: String containing name of the user.
			:param access: RO | RW Defines the access right a user can have.
			:param level: NOAuth | AUTH | PRIVacy Defines the security level.
			:param auth_pwd: String containing the authentication password.
			:param priv_pwd: String containing the privacy password.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('access', access, DataType.Enum, enums.AccessType), ArgSingle('level', level, DataType.Enum, enums.UserLevel), ArgSingle('auth_pwd', auth_pwd, DataType.String, None, is_optional=True), ArgSingle('priv_pwd', priv_pwd, DataType.String, None, is_optional=True))
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:USM:USER {param}'.rstrip())

	def delete(self, name: str) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:USM:USER:DELete \n
		Snippet: driver.system.communicate.snmp.usm.user.delete(name = '1') \n
		This command deletes a specific SNMP user profile. \n
			:param name: String containing name of SNMP user profile to be deleted.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:USM:USER:DELete {param}')

	def delete_all(self) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:USM:USER:DELete:ALL \n
		Snippet: driver.system.communicate.snmp.usm.user.delete_all() \n
		This command deletes all SNMP user profiles. \n
		"""
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:USM:USER:DELete:ALL')

	def delete_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:USM:USER:DELete:ALL \n
		Snippet: driver.system.communicate.snmp.usm.user.delete_all_with_opc() \n
		This command deletes all SNMP user profiles. \n
		Same as delete_all, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:COMMunicate:SNMP:USM:USER:DELete:ALL', opc_timeout_ms)

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
