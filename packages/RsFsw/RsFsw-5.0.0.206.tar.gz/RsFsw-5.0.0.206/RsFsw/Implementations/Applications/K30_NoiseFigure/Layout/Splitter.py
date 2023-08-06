from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Splitter:
	"""Splitter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("splitter", core, parent)

	def set(self, index_1: float, index_2: float, position: float) -> None:
		"""SCPI: LAYout:SPLitter \n
		Snippet: driver.applications.k30NoiseFigure.layout.splitter.set(index_1 = 1.0, index_2 = 1.0, position = 1.0) \n
		This command changes the position of a splitter and thus controls the size of the windows on each side of the splitter.
		Compared to the method RsFsw.Applications.K17_Mcgd.Display.Window.Size.set command, the method RsFsw.Applications.
		K17_Mcgd.Layout.Splitter.set changes the size of all windows to either side of the splitter permanently, it does not just
		maximize a single window temporarily. Note that windows must have a certain minimum size. If the position you define
		conflicts with the minimum size of any of the affected windows, the command will not work, but does not return an error. \n
			:param index_1: The index of one window the splitter controls.
			:param index_2: The index of a window on the other side of the splitter.
			:param position: New vertical or horizontal position of the splitter as a fraction of the screen area (without channel and status bar and softkey menu) . The point of origin (x = 0, y = 0) is in the lower left corner of the screen. The end point (x = 100, y = 100) is in the upper right corner of the screen. (See Figure 'SmartGrid coordinates for remote control of the splitters'.) The direction in which the splitter is moved depends on the screen layout. If the windows are positioned horizontally, the splitter also moves horizontally. If the windows are positioned vertically, the splitter also moves vertically. Range: 0 to 100
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index_1', index_1, DataType.Float), ArgSingle('index_2', index_2, DataType.Float), ArgSingle('position', position, DataType.Float))
		self._core.io.write_with_opc(f'LAYout:SPLitter {param}'.rstrip())

	# noinspection PyTypeChecker
	class SplitterStruct(StructBase):
		"""Response structure. Fields: \n
			- Index_1: float: The index of one window the splitter controls.
			- Index_2: float: The index of a window on the other side of the splitter.
			- Position: float: New vertical or horizontal position of the splitter as a fraction of the screen area (without channel and status bar and softkey menu) . The point of origin (x = 0, y = 0) is in the lower left corner of the screen. The end point (x = 100, y = 100) is in the upper right corner of the screen. (See Figure 'SmartGrid coordinates for remote control of the splitters'.) The direction in which the splitter is moved depends on the screen layout. If the windows are positioned horizontally, the splitter also moves horizontally. If the windows are positioned vertically, the splitter also moves vertically. Range: 0 to 100"""
		__meta_args_list = [
			ArgStruct.scalar_float('Index_1'),
			ArgStruct.scalar_float('Index_2'),
			ArgStruct.scalar_float('Position')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index_1: float = None
			self.Index_2: float = None
			self.Position: float = None

	def get(self) -> SplitterStruct:
		"""SCPI: LAYout:SPLitter \n
		Snippet: value: SplitterStruct = driver.applications.k30NoiseFigure.layout.splitter.get() \n
		This command changes the position of a splitter and thus controls the size of the windows on each side of the splitter.
		Compared to the method RsFsw.Applications.K17_Mcgd.Display.Window.Size.set command, the method RsFsw.Applications.
		K17_Mcgd.Layout.Splitter.set changes the size of all windows to either side of the splitter permanently, it does not just
		maximize a single window temporarily. Note that windows must have a certain minimum size. If the position you define
		conflicts with the minimum size of any of the affected windows, the command will not work, but does not return an error. \n
			:return: structure: for return value, see the help for SplitterStruct structure arguments."""
		return self._core.io.query_struct_with_opc(f'LAYout:SPLitter?', self.__class__.SplitterStruct())
