from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, frequency: List[float], bandwidth: List[float], sweep_time: List[float]) -> None:
		"""SCPI: [SENSe]:BWIDth:LIST:DATA \n
		Snippet: driver.applications.k30NoiseFigure.sense.bandwidth.listPy.data.set(frequency = [1.1, 2.2, 3.3], bandwidth = [1.1, 2.2, 3.3], sweep_time = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param frequency: No help available
			:param bandwidth: No help available
			:param sweep_time: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None), ArgSingle.as_open_list('bandwidth', bandwidth, DataType.FloatList, None), ArgSingle.as_open_list('sweep_time', sweep_time, DataType.FloatList, None))
		self._core.io.write(f'SENSe:BWIDth:LIST:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: No parameter help available
			- Bandwidth: List[float]: No parameter help available
			- Sweep_Time: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Bandwidth', DataType.FloatList, None, False, True, 1),
			ArgStruct('Sweep_Time', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Bandwidth: List[float] = None
			self.Sweep_Time: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: [SENSe]:BWIDth:LIST:DATA \n
		Snippet: value: DataStruct = driver.applications.k30NoiseFigure.sense.bandwidth.listPy.data.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:BWIDth:LIST:DATA?', self.__class__.DataStruct())
