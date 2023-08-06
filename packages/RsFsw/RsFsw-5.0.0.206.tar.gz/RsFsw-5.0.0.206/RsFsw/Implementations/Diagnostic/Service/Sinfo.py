from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sinfo:
	"""Sinfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:SINFo \n
		Snippet: value: str = driver.diagnostic.service.sinfo.get() \n
		This command creates a *.zip file with important support information. The *.zip file contains the system configuration
		information ('device footprint') , the current eeprom data and a screenshot of the screen display (if available) . This
		data is stored to the C:/R_S/INSTR/USER directory on the instrument. As a result of this command, the created file name
		(including the drive and path) is returned. You can use the resulting file name information as a parameter for the method
		RsFsw.MassMemory.copy command to store the file on the controller PC. (See method RsFsw.MassMemory.copy) If you contact
		the Rohde & Schwarz support to get help for a certain problem, send this file to the support in order to identify and
		solve the problem faster. \n
			:return: filename: C:/R_S/INSTR/USER/R&S Device ID_CurrentDate_CurrentTime String containing the drive, path and file name of the created support file, where the file name consists of the following elements: R&S Device ID: The unique R&S device ID indicated in the 'Versions + Options' information (See 'Licensing, versions and options') CurrentDate: The date on which the file is created (YYYYMMDD) CurrentTime: The time at which the file is created (HHMMSS)"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:SINFo?')
		return trim_str_response(response)
