from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Icon:
	"""Icon commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icon", core, parent)

	def set(self, icon_path: str, icon_index: str) -> None:
		"""SCPI: SYSTem:PLUGin:APPStarter:ICON \n
		Snippet: driver.system.plugin.appStarter.icon.set(icon_path = '1', icon_index = '1') \n
		Defines an icon for the selected application to be displayed in the 'Application Starter' dialog box. \n
			:param icon_path: Path and file name for icon
			:param icon_index: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('icon_path', icon_path, DataType.String), ArgSingle('icon_index', icon_index, DataType.String))
		self._core.io.write(f'SYSTem:PLUGin:APPStarter:ICON {param}'.rstrip())

	# noinspection PyTypeChecker
	class IconStruct(StructBase):
		"""Response structure. Fields: \n
			- Icon_Path: str: Path and file name for icon
			- Icon_Index: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Icon_Path'),
			ArgStruct.scalar_str('Icon_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Icon_Path: str = None
			self.Icon_Index: str = None

	def get(self) -> IconStruct:
		"""SCPI: SYSTem:PLUGin:APPStarter:ICON \n
		Snippet: value: IconStruct = driver.system.plugin.appStarter.icon.get() \n
		Defines an icon for the selected application to be displayed in the 'Application Starter' dialog box. \n
			:return: structure: for return value, see the help for IconStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:PLUGin:APPStarter:ICON?', self.__class__.IconStruct())
