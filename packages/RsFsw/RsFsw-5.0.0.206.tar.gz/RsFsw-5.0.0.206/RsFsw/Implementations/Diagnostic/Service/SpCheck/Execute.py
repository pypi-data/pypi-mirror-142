from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def get(self) -> bool:
		"""SCPI: DIAGnostic:SERVice:SPCHeck:EXECute \n
		Snippet: value: bool = driver.diagnostic.service.spCheck.execute.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:SPCHeck:EXECute?')
		return Conversions.str_to_bool(response)
