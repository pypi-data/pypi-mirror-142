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
		"""SCPI: DIAGnostic:SERVice:SPCHeck:RESult \n
		Snippet: value: str = driver.diagnostic.service.spCheck.result.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:SPCHeck:RESult?')
		return trim_str_response(response)
