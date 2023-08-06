from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Description:
	"""Description commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("description", core, parent)

	def set(self, arg_0: str) -> None:
		"""SCPI: HCOPy:TREPort:DESCription \n
		Snippet: driver.hardCopy.treport.description.set(arg_0 = '1') \n
		This command defines the description of the test report as shown on its title page. \n
			:param arg_0: String containing the description of the test report.
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'HCOPy:TREPort:DESCription {param}')

	def get(self) -> str:
		"""SCPI: HCOPy:TREPort:DESCription \n
		Snippet: value: str = driver.hardCopy.treport.description.get() \n
		This command defines the description of the test report as shown on its title page. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'HCOPy:TREPort:DESCription?')
		return trim_str_response(response)
