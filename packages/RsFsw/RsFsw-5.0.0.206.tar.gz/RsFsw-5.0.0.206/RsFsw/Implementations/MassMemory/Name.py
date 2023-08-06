from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, arg_0: str) -> None:
		"""SCPI: MMEMory:NAME \n
		Snippet: driver.massMemory.name.set(arg_0 = '1') \n
		This command has several purposes, depending on the context it is used in.
			- It creates a new and empty file.
			- It defines the file name for screenshots taken with method RsFsw.HardCopy.Immediate.set. Note that you have to route the printer output to a file. \n
			:param arg_0: String containing the path and name of the target file.
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'MMEMory:NAME {param}')

	def get(self) -> str:
		"""SCPI: MMEMory:NAME \n
		Snippet: value: str = driver.massMemory.name.get() \n
		This command has several purposes, depending on the context it is used in.
			- It creates a new and empty file.
			- It defines the file name for screenshots taken with method RsFsw.HardCopy.Immediate.set. Note that you have to route the printer output to a file. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'MMEMory:NAME?')
		return trim_str_response(response)
