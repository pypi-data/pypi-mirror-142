from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Area:
	"""Area commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("area", core, parent)

	def set(self, x_1: float, y_1: float, x_2: float, y_2: float, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:AREA \n
		Snippet: driver.display.window.subwindow.zoom.area.set(x_1 = 1.0, y_1 = 1.0, x_2 = 1.0, y_2 = 1.0, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command defines the zoom area. To define a zoom area, you first have to turn the zoom on. \n
			:param x_1: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			:param y_1: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			:param x_2: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			:param y_2: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('x_1', x_1, DataType.Float), ArgSingle('y_1', y_1, DataType.Float), ArgSingle('x_2', x_2, DataType.Float), ArgSingle('y_2', y_2, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:AREA {param}'.rstrip())

	# noinspection PyTypeChecker
	class AreaStruct(StructBase):
		"""Response structure. Fields: \n
			- X_1: float: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			- Y_1: float: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			- X_2: float: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT
			- Y_2: float: Diagram coordinates in % of the complete diagram that define the zoom area. The lower left corner is the origin of coordinate system. The upper right corner is the end point of the system. Range: 0 to 100, Unit: PCT"""
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

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> AreaStruct:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:AREA \n
		Snippet: value: AreaStruct = driver.display.window.subwindow.zoom.area.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command defines the zoom area. To define a zoom area, you first have to turn the zoom on. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:return: structure: for return value, see the help for AreaStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		return self._core.io.query_struct(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:AREA?', self.__class__.AreaStruct())
