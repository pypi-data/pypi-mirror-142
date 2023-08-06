from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, file_spec: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:PATH \n
		Snippet: driver.system.plugin.appStarter.path.set(file_spec = '1') \n
		Defines a new path to the selected application. \n
			:param file_spec: Path, file name, and extension of the application
		"""
		param = Conversions.value_to_quoted_str(file_spec)
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:PATH {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:PLUGin:APPStarter:PATH \n
		Snippet: value: str = driver.system.plugin.appStarter.path.get() \n
		Defines a new path to the selected application. \n
			:return: file_spec: Path, file name, and extension of the application"""
		response = self._core.io.query_str(f'SYSTem:PLUGin:APPStarter:PATH?')
		return trim_str_response(response)
