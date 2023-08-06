from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Contact:
	"""Contact commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("contact", core, parent)

	def set(self, contact_info: str) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:CONTact \n
		Snippet: driver.system.communicate.snmp.contact.set(contact_info = '1') \n
		This command sets the SNMP contact information for the administrator. You can also set the contact information via SNMP
		if you do not set it via SCPI. \n
			:param contact_info: String containing SNMP contact.
		"""
		param = Conversions.value_to_quoted_str(contact_info)
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:CONTact {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:SNMP:CONTact \n
		Snippet: value: str = driver.system.communicate.snmp.contact.get() \n
		This command sets the SNMP contact information for the administrator. You can also set the contact information via SNMP
		if you do not set it via SCPI. \n
			:return: contact_info: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:SNMP:CONTact?')
		return trim_str_response(response)
