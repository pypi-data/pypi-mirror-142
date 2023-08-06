from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Long:
	"""Long commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("long", core, parent)

	def set(self, directory: str) -> None:
		"""SCPI: MMEMory:CATalog:LONG \n
		Snippet: driver.massMemory.catalog.long.set(directory = '1') \n
		This command returns the contents of a particular directory with additional information about the files. \n
			:param directory: String containing the path and directory. If you leave out the path, the command returns the contents of the directory selected with method RsFsw.MassMemory.CurrentDirectory.set. The path may be relative or absolute. Using wildcards ('*') is possible to query a certain type of files only.
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'MMEMory:CATalog:LONG {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:CATalog:LONG \n
		Snippet: value: str = driver.massMemory.catalog.long.get() \n
		This command returns the contents of a particular directory with additional information about the files. \n
			:return: directory: String containing the path and directory. If you leave out the path, the command returns the contents of the directory selected with method RsFsw.MassMemory.CurrentDirectory.set. The path may be relative or absolute. Using wildcards ('*') is possible to query a certain type of files only."""
		response = self._core.io.query_str(f'MMEMory:CATalog:LONG?')
		return trim_str_response(response)
