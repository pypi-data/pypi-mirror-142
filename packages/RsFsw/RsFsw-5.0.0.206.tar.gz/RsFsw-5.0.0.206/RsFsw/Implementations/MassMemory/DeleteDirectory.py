from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeleteDirectory:
	"""DeleteDirectory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deleteDirectory", core, parent)

	def set(self, arg_0: str) -> None:
		"""SCPI: MMEMory:RDIRectory \n
		Snippet: driver.massMemory.deleteDirectory.set(arg_0 = '1') \n
		This command deletes the indicated directory. \n
			:param arg_0: String containing the path of the directory to delete. Note that the directory you want to remove must be empty.
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'MMEMory:RDIRectory {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:RDIRectory \n
		Snippet: value: str = driver.massMemory.deleteDirectory.get() \n
		This command deletes the indicated directory. \n
			:return: arg_0: String containing the path of the directory to delete. Note that the directory you want to remove must be empty."""
		response = self._core.io.query_str(f'MMEMory:RDIRectory?')
		return trim_str_response(response)
