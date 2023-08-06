from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Params:
	"""Params commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("params", core, parent)

	def set(self, params: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:PARams \n
		Snippet: driver.system.plugin.appStarter.params.set(params = '1') \n
		Defines parameters that are provided with the application for execution, for example arguments for a custom script. \n
			:param params: No help available
		"""
		param = Conversions.value_to_quoted_str(params)
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:PARams {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:PLUGin:APPStarter:PARams \n
		Snippet: value: str = driver.system.plugin.appStarter.params.get() \n
		Defines parameters that are provided with the application for execution, for example arguments for a custom script. \n
			:return: params: No help available"""
		response = self._core.io.query_str(f'SYSTem:PLUGin:APPStarter:PARams?')
		return trim_str_response(response)
