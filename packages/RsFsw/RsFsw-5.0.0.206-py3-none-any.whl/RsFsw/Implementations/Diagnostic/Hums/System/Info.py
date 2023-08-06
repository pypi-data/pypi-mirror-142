from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	def get(self) -> bytes:
		"""SCPI: DIAGnostic:HUMS:SYSTem:INFO \n
		Snippet: value: bytes = driver.diagnostic.hums.system.info.get() \n
		No command help available \n
			:return: system_info: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:HUMS:SYSTem:INFO?')
		return response
