from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentDirectory:
	"""CurrentDirectory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("currentDirectory", core, parent)

	def set(self, directory: str) -> None:
		"""SCPI: MMEMory:CDIRectory \n
		Snippet: driver.massMemory.currentDirectory.set(directory = '1') \n
		This command changes the current directory. \n
			:param directory: String containing the path to another directory. The path may be relative or absolute.
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write_with_opc(f'MMEMory:CDIRectory {param}')
