from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Area:
	"""Area commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("area", core, parent)

	def set(self, x_1: float, y_1: float, x_2: float, y_2: float, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>:AREA \n
		Snippet: driver.applications.k91Wlan.display.window.subwindow.zoom.multiple.area.set(x_1 = 1.0, y_1 = 1.0, x_2 = 1.0, y_2 = 1.0, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		No command help available \n
			:param x_1: No help available
			:param y_1: No help available
			:param x_2: No help available
			:param y_2: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('x_1', x_1, DataType.Float), ArgSingle('y_1', y_1, DataType.Float), ArgSingle('x_2', x_2, DataType.Float), ArgSingle('y_2', y_2, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:AREA {param}'.rstrip())

	# noinspection PyTypeChecker
	class AreaStruct(StructBase):
		"""Response structure. Fields: \n
			- X_1: float: No parameter help available
			- Y_1: float: No parameter help available
			- X_2: float: No parameter help available
			- Y_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('X_1'),
			ArgStruct.scalar_float('Y_1'),
			ArgStruct.scalar_float('X_2'),
			ArgStruct.scalar_float('Y_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.X_1: float = None
			self.Y_1: float = None
			self.X_2: float = None
			self.Y_2: float = None

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> AreaStruct:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>:AREA \n
		Snippet: value: AreaStruct = driver.applications.k91Wlan.display.window.subwindow.zoom.multiple.area.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
			:return: structure: for return value, see the help for AreaStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		return self._core.io.query_struct(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:AREA?', self.__class__.AreaStruct())
