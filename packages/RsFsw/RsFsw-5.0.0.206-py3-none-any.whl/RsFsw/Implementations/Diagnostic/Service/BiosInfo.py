from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BiosInfo:
	"""BiosInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("biosInfo", core, parent)

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:BIOSinfo \n
		Snippet: value: str = driver.diagnostic.service.biosInfo.get() \n
		This command queries the BIOS version of the CPU board. \n
			:return: bios_information: String containing the BIOS version."""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:BIOSinfo?')
		return trim_str_response(response)
