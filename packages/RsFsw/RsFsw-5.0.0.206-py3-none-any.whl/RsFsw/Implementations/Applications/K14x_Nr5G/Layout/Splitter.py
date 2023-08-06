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

	def set(self, arg_0: float, arg_1: float, arg_2: float) -> None:
		"""SCPI: LAYout:SPLitter \n
		Snippet: driver.applications.k14Xnr5G.layout.splitter.set(arg_0 = 1.0, arg_1 = 1.0, arg_2 = 1.0) \n
		This command changes the position of a splitter and thus controls the size of the windows on each side of the splitter.
		Compared to the method RsFsw.Applications.K17_Mcgd.Display.Window.Size.set command, the method RsFsw.Applications.
		K17_Mcgd.Layout.Splitter.set changes the size of all windows to either side of the splitter permanently, it does not just
		maximize a single window temporarily. Note that windows must have a certain minimum size. If the position you define
		conflicts with the minimum size of any of the affected windows, the command will not work, but does not return an error. \n
			:param arg_0: No help available
			:param arg_1: No help available
			:param arg_2: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Float), ArgSingle('arg_1', arg_1, DataType.Float), ArgSingle('arg_2', arg_2, DataType.Float))
		self._core.io.write_with_opc(f'LAYout:SPLitter {param}'.rstrip())

	# noinspection PyTypeChecker
	class SplitterStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: float: No parameter help available
			- Arg_1: float: No parameter help available
			- Arg_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Arg_0'),
			ArgStruct.scalar_float('Arg_1'),
			ArgStruct.scalar_float('Arg_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: float = None
			self.Arg_1: float = None
			self.Arg_2: float = None

	def get(self) -> SplitterStruct:
		"""SCPI: LAYout:SPLitter \n
		Snippet: value: SplitterStruct = driver.applications.k14Xnr5G.layout.splitter.get() \n
		This command changes the position of a splitter and thus controls the size of the windows on each side of the splitter.
		Compared to the method RsFsw.Applications.K17_Mcgd.Display.Window.Size.set command, the method RsFsw.Applications.
		K17_Mcgd.Layout.Splitter.set changes the size of all windows to either side of the splitter permanently, it does not just
		maximize a single window temporarily. Note that windows must have a certain minimum size. If the position you define
		conflicts with the minimum size of any of the affected windows, the command will not work, but does not return an error. \n
			:return: structure: for return value, see the help for SplitterStruct structure arguments."""
		return self._core.io.query_struct_with_opc(f'LAYout:SPLitter?', self.__class__.SplitterStruct())
