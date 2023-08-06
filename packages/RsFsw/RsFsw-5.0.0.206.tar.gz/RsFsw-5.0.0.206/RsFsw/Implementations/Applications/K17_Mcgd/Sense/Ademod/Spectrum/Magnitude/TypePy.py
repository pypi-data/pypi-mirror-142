from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, trace_1: enums.TraceModeA, trace_2: enums.TraceModeA, trace_3: enums.TraceModeA) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum[:MAGNitude][:TYPE] \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.spectrum.magnitude.typePy.set(trace_1 = enums.TraceModeA.AVERage, trace_2 = enums.TraceModeA.AVERage, trace_3 = enums.TraceModeA.AVERage) \n
		This command sets the modes of the first three traces of magnitude windows. Note that this command is maintained for
		compatibility reasons only. Use method RsFsw.Display.Window.Trace.Mode.set for new remote control programs. \n
			:param trace_1: WRITe | AVERage | MINHold | MAXHold | VIEW | OFF
			:param trace_2: WRITe | AVERage | MINHold | MAXHold | VIEW | OFF
			:param trace_3: WRITe | AVERage | MINHold | MAXHold | VIEW | OFF
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('trace_1', trace_1, DataType.Enum, enums.TraceModeA), ArgSingle('trace_2', trace_2, DataType.Enum, enums.TraceModeA), ArgSingle('trace_3', trace_3, DataType.Enum, enums.TraceModeA))
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:MAGNitude:TYPE {param}'.rstrip())

	# noinspection PyTypeChecker
	class TypePyStruct(StructBase):
		"""Response structure. Fields: \n
			- Trace_1: enums.TraceModeA: WRITe | AVERage | MINHold | MAXHold | VIEW | OFF
			- Trace_2: enums.TraceModeA: WRITe | AVERage | MINHold | MAXHold | VIEW | OFF
			- Trace_3: enums.TraceModeA: WRITe | AVERage | MINHold | MAXHold | VIEW | OFF"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Trace_1', enums.TraceModeA),
			ArgStruct.scalar_enum('Trace_2', enums.TraceModeA),
			ArgStruct.scalar_enum('Trace_3', enums.TraceModeA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Trace_1: enums.TraceModeA = None
			self.Trace_2: enums.TraceModeA = None
			self.Trace_3: enums.TraceModeA = None

	def get(self) -> TypePyStruct:
		"""SCPI: [SENSe]:ADEMod:SPECtrum[:MAGNitude][:TYPE] \n
		Snippet: value: TypePyStruct = driver.applications.k17Mcgd.sense.ademod.spectrum.magnitude.typePy.get() \n
		This command sets the modes of the first three traces of magnitude windows. Note that this command is maintained for
		compatibility reasons only. Use method RsFsw.Display.Window.Trace.Mode.set for new remote control programs. \n
			:return: structure: for return value, see the help for TypePyStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:ADEMod:SPECtrum:MAGNitude:TYPE?', self.__class__.TypePyStruct())
