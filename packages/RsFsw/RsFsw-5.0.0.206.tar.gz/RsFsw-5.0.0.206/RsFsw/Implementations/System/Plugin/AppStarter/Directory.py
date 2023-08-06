from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Directory:
	"""Directory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("directory", core, parent)

	def set(self, working_dir: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:DIRectory \n
		Snippet: driver.system.plugin.appStarter.directory.set(working_dir = '1') \n
		Defines the working directory used by the selected application. \n
			:param working_dir: No help available
		"""
		param = Conversions.value_to_quoted_str(working_dir)
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:DIRectory {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:PLUGin:APPStarter:DIRectory \n
		Snippet: value: str = driver.system.plugin.appStarter.directory.get() \n
		Defines the working directory used by the selected application. \n
			:return: working_dir: No help available"""
		response = self._core.io.query_str(f'SYSTem:PLUGin:APPStarter:DIRectory?')
		return trim_str_response(response)
