from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Name:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, display_name: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:NAME \n
		Snippet: driver.system.plugin.appStarter.name.set(display_name = '1') \n
		Defines the name of the application as displayed in the 'Application Starter' dialog box. \n
			:param display_name: No help available
		"""
		param = Conversions.value_to_quoted_str(display_name)
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:NAME {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:PLUGin:APPStarter:NAME \n
		Snippet: value: str = driver.system.plugin.appStarter.name.get() \n
		Defines the name of the application as displayed in the 'Application Starter' dialog box. \n
			:return: display_name: No help available"""
		response = self._core.io.query_str(f'SYSTem:PLUGin:APPStarter:NAME?')
		return trim_str_response(response)
