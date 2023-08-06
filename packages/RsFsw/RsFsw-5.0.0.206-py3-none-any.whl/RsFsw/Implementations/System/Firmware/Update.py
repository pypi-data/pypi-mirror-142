from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Update:
	"""Update commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("update", core, parent)

	def set(self, directory: str) -> None:
		"""SCPI: SYSTem:FIRMware:UPDate \n
		Snippet: driver.system.firmware.update.set(directory = '1') \n
		This command starts a firmware update using the *.msi files in the selected directory. The default path is D:/FW_UPDATE.
		The path is changed via the method RsFsw.MassMemory.Comment.set command. To store the update files the MMEMory:DATA
		command is used. Only user accounts with administrator rights can perform a firmware update. \n
			:param directory: No help available
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'SYSTem:FIRMware:UPDate {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:FIRMware:UPDate \n
		Snippet: value: str = driver.system.firmware.update.get() \n
		This command starts a firmware update using the *.msi files in the selected directory. The default path is D:/FW_UPDATE.
		The path is changed via the method RsFsw.MassMemory.Comment.set command. To store the update files the MMEMory:DATA
		command is used. Only user accounts with administrator rights can perform a firmware update. \n
			:return: directory: No help available"""
		response = self._core.io.query_str(f'SYSTem:FIRMware:UPDate?')
		return trim_str_response(response)
