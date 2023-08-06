from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Version:
	"""Version commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("version", core, parent)

	def set(self, snmp_version: enums.SnmpVersion) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:VERSion \n
		Snippet: driver.system.communicate.snmp.version.set(snmp_version = enums.SnmpVersion.DEFault) \n
		This command selects the SNMP version. \n
			:param snmp_version: OFF | V12 | V123 | V3 | DEFault OFF SNMP communication is off. V12 SNMP communication with SNMPv2 or lower. V123 SNMP communication with SNMPv2 and SNMPv3. V3 SNMP communication with SNMPv3.
		"""
		param = Conversions.enum_scalar_to_str(snmp_version, enums.SnmpVersion)
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:VERSion {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SnmpVersion:
		"""SCPI: SYSTem:COMMunicate:SNMP:VERSion \n
		Snippet: value: enums.SnmpVersion = driver.system.communicate.snmp.version.get() \n
		This command selects the SNMP version. \n
			:return: snmp_version: OFF | V12 | V123 | V3 | DEFault OFF SNMP communication is off. V12 SNMP communication with SNMPv2 or lower. V123 SNMP communication with SNMPv2 and SNMPv3. V3 SNMP communication with SNMPv3."""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:SNMP:VERSion?')
		return Conversions.str_to_scalar_enum(response, enums.SnmpVersion)
