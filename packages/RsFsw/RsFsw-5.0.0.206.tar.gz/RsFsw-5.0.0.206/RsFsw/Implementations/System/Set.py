from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Set:
	"""Set commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)

	def set(self, block_data: bytes) -> None:
		"""SCPI: SYSTem:SET \n
		Snippet: driver.system.set.set(block_data = b'ABCDEFGH') \n
		No command help available \n
			:param block_data: No help available
		"""
		self._core.io.write_bin_block(f'SYSTem:SET ', block_data)

	def get(self) -> bytes:
		"""SCPI: SYSTem:SET \n
		Snippet: value: bytes = driver.system.set.get() \n
		No command help available \n
			:return: block_data: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:SET?')
		return response
