from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ro:
	"""Ro commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ro", core, parent)

	def set(self, community: str) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:COMMunity:RO \n
		Snippet: driver.system.communicate.snmp.community.ro.set(community = '1') \n
		This command sets the SNMP community string for read-only access.
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- Select an SNMP version that supports communities (method RsFsw.System.Communicate.Snmp.Version.set) . \n
			:param community: String containing the community name.
		"""
		param = Conversions.value_to_quoted_str(community)
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:COMMunity:RO {param}')
