from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> bytes:
		"""SCPI: DIAGnostic:HUMS:TAGS:ALL \n
		Snippet: value: bytes = driver.diagnostic.hums.tags.all.get() \n
		This command returns all key-value tags that you have assigend to the instrument. Depending on the set data format, the
		queried data is either displayed in XML or JSON format. For more information about setting the data format, see method
		RsFsw.Diagnostic.Hums.FormatPy.set. \n
			:return: tags_info: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:HUMS:TAGS:ALL?')
		return response
