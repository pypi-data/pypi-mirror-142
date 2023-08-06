from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, frequency_enr: List[float], enr: List[float]) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TABLe[:DATA] \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.table.data.set(frequency_enr = [1.1, 2.2, 3.3], enr = [1.1, 2.2, 3.3]) \n
		This command defines the contents of the currently selected ENR table. Define an ENR for all measurement points.
		Each entry of the ENR table consists of one measurement point and the corresponding ENR. The individual values are
		separated by commas or spaces. The table can contain up to 10001 entries. If you create a new table with this command, it
		overwrites the current entries of the frequency list.
		To select the ENR table to edit, use [SENSe:]CORRection:ENR[:MEASurement]:TABLe[:DATA]. \n
			:param frequency_enr: Frequency of the measurement point. Range: 0 Hz to 999.99 GHz, Unit: HZ
			:param enr: Unit: DB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('frequency_enr', frequency_enr, DataType.FloatList, None), ArgSingle.as_open_list('enr', enr, DataType.FloatList, None))
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:TABLe:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency_Enr: List[float]: Frequency of the measurement point. Range: 0 Hz to 999.99 GHz, Unit: HZ
			- Enr: List[float]: Unit: DB"""
		__meta_args_list = [
			ArgStruct('Frequency_Enr', DataType.FloatList, None, False, True, 1),
			ArgStruct('Enr', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency_Enr: List[float] = None
			self.Enr: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TABLe[:DATA] \n
		Snippet: value: DataStruct = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.table.data.get() \n
		This command defines the contents of the currently selected ENR table. Define an ENR for all measurement points.
		Each entry of the ENR table consists of one measurement point and the corresponding ENR. The individual values are
		separated by commas or spaces. The table can contain up to 10001 entries. If you create a new table with this command, it
		overwrites the current entries of the frequency list.
		To select the ENR table to edit, use [SENSe:]CORRection:ENR[:MEASurement]:TABLe[:DATA]. \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:CORRection:ENR:MEASurement:TABLe:DATA?', self.__class__.DataStruct())
