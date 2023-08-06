from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> bytes:
		"""SCPI: SYSTem:HELP:SYNTax:ALL \n
		Snippet: value: bytes = driver.system.help.syntax.all.get() \n
		No command help available \n
			:return: syntax: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'SYSTem:HELP:SYNTax:ALL?')
		return response
