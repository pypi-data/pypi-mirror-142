from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Headers:
	"""Headers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("headers", core, parent)

	def get(self) -> bytes:
		"""SCPI: SYSTem:HELP:HEADers \n
		Snippet: value: bytes = driver.system.help.headers.get() \n
		No command help available \n
			:return: header: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:HELP:HEADers?')
		return response
