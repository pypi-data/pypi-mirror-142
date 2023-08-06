from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LastResult:
	"""LastResult commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lastResult", core, parent)

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:SFUNction:LASTresult \n
		Snippet: value: str = driver.diagnostic.service.sfunction.lastResult.get() \n
		This command queries the results of the most recent service function you have used. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:SFUNction:LASTresult?')
		return trim_str_response(response)
