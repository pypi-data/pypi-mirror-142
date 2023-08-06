from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VersionInfo:
	"""VersionInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("versionInfo", core, parent)

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:VERSinfo \n
		Snippet: value: str = driver.diagnostic.service.versionInfo.get() \n
		This command queries information about the hardware and software components. \n
			:return: information: String containing the version of hardware and software components including the types of licenses for installed options."""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:VERSinfo?')
		return trim_str_response(response)
