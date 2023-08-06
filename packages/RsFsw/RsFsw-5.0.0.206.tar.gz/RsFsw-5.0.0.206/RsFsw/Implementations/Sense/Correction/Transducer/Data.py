from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, frequency: List[float], level: List[float]) -> None:
		"""SCPI: [SENSe]:CORRection:TRANsducer:DATA \n
		Snippet: driver.sense.correction.transducer.data.set(frequency = [1.1, 2.2, 3.3], level = [1.1, 2.2, 3.3]) \n
		This command configures transducer factors for specific trace points. A set of transducer factors defines an interpolated
		transducer line and can be stored on the instrument. For details see 'Basics on transducer factors'. \n
			:param frequency: The unit for Frequency is Hz, which may or may not be omitted. Frequencies have to be sorted in ascending order. Unit: Hz
			:param level: The unit for Level depends on[SENSe:]CORRection:TRANsducer:UNIT .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None), ArgSingle.as_open_list('level', level, DataType.FloatList, None))
		self._core.io.write(f'SENSe:CORRection:TRANsducer:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: The unit for Frequency is Hz, which may or may not be omitted. Frequencies have to be sorted in ascending order. Unit: Hz
			- Level: List[float]: The unit for Level depends on[SENSe:]CORRection:TRANsducer:UNIT ."""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Level', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Level: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: [SENSe]:CORRection:TRANsducer:DATA \n
		Snippet: value: DataStruct = driver.sense.correction.transducer.data.get() \n
		This command configures transducer factors for specific trace points. A set of transducer factors defines an interpolated
		transducer line and can be stored on the instrument. For details see 'Basics on transducer factors'. \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:CORRection:TRANsducer:DATA?', self.__class__.DataStruct())
