from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Storage:
	"""Storage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("storage", core, parent)

	def get(self) -> bytes:
		"""SCPI: DIAGnostic:HUMS:STORage \n
		Snippet: value: bytes = driver.diagnostic.hums.storage.get() \n
		No command help available \n
			:return: storage_info: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:HUMS:STORage?')
		return response
