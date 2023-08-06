from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	def get(self) -> str:
		"""SCPI: HCOPy:TREPort:ITEM:LIST \n
		Snippet: value: str = driver.hardCopy.treport.item.listPy.get() \n
		This command queries the selected information to be included in the test report for a specific channel type. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'HCOPy:TREPort:ITEM:LIST?')
		return trim_str_response(response)
