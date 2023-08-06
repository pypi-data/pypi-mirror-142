from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:STESt:RESult \n
		Snippet: value: str = driver.diagnostic.service.stest.result.get() \n
		This command queries the self-test results. \n
			:return: results: String of data containing the results. The rows of the self-test result table are separated by commas."""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:STESt:RESult?')
		return trim_str_response(response)
