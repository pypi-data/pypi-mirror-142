from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: MMEMory:DELete:IMMediate \n
		Snippet: driver.massMemory.delete.immediate.set(filename = '1') \n
		This command deletes a file. \n
			:param filename: String containing the path and file name of the file to delete. The path may be relative or absolute.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'MMEMory:DELete:IMMediate {param}')
