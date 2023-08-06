from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("add", core, parent)

	def set(self, application_group: str, display_name: str, file_spec: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:ADD \n
		Snippet: driver.system.plugin.appStarter.add.set(application_group = '1', display_name = '1', file_spec = '1') \n
		Adds an application to the specified group in the Application Starter dialog box. \n
			:param application_group: 'External' | 'User' The group (tab) of applications in the Application Starter that the application belongs to. 'External' External Applications 'User' User Applications
			:param display_name: Name of the application in the Application Starter
			:param file_spec: Path and file name of the application
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('application_group', application_group, DataType.String), ArgSingle('display_name', display_name, DataType.String), ArgSingle('file_spec', file_spec, DataType.String))
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:ADD {param}'.rstrip())
