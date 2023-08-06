from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Location:
	"""Location commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("location", core, parent)

	def set(self, location: str) -> None:
		"""SCPI: SYSTem:COMMunicate:SNMP:LOCation \n
		Snippet: driver.system.communicate.snmp.location.set(location = '1') \n
		This command sets the SNMP location information for the administrator. You can also set the location information via SNMP
		if you do not set it via SCPI. \n
			:param location: String containing SNMP location.
		"""
		param = Conversions.value_to_quoted_str(location)
		self._core.io.write(f'SYSTem:COMMunicate:SNMP:LOCation {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:SNMP:LOCation \n
		Snippet: value: str = driver.system.communicate.snmp.location.get() \n
		This command sets the SNMP location information for the administrator. You can also set the location information via SNMP
		if you do not set it via SCPI. \n
			:return: location: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:SNMP:LOCation?')
		return trim_str_response(response)
