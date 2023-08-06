from typing import List

from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, frequency: List[float], thot: List[float], tcold: List[float]) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TABLe:TEMPerature[:DATA] \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.table.temperature.data.set(frequency = [1.1, 2.2, 3.3], thot = [1.1, 2.2, 3.3], tcold = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param frequency: Unit: HZ
			:param thot: Unit: K
			:param tcold: Unit: K
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None), ArgSingle.as_open_list('thot', thot, DataType.FloatList, None), ArgSingle.as_open_list('tcold', tcold, DataType.FloatList, None))
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:TABLe:TEMPerature:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: Unit: HZ
			- Thot: List[float]: Unit: K
			- Tcold: List[float]: Unit: K"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Thot', DataType.FloatList, None, False, True, 1),
			ArgStruct('Tcold', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Thot: List[float] = None
			self.Tcold: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TABLe:TEMPerature[:DATA] \n
		Snippet: value: DataStruct = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.table.temperature.data.get() \n
		No command help available \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:CORRection:ENR:MEASurement:TABLe:TEMPerature:DATA?', self.__class__.DataStruct())
