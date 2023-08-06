from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MakeDirectory:
	"""MakeDirectory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("makeDirectory", core, parent)

	def set(self, directory: str) -> None:
		"""SCPI: MMEMory:MDIRectory \n
		Snippet: driver.massMemory.makeDirectory.set(directory = '1') \n
		This command creates a new directory. \n
			:param directory: String containing the path and new directory name The path may be relative or absolute.
		"""
		param = Conversions.value_to_quoted_str(directory)
		self._core.io.write(f'MMEMory:MDIRectory {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:MDIRectory \n
		Snippet: value: str = driver.massMemory.makeDirectory.get() \n
		This command creates a new directory. \n
			:return: directory: String containing the path and new directory name The path may be relative or absolute."""
		response = self._core.io.query_str(f'MMEMory:MDIRectory?')
		return trim_str_response(response)
