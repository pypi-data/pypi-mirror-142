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

	def set(self, frequency: List[float], loss: List[float]) -> None:
		"""SCPI: [SENSe]:CORRection:LOSS:OUTPut:TABLe[:DATA] \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.loss.output.table.data.set(frequency = [1.1, 2.2, 3.3], loss = [1.1, 2.2, 3.3]) \n
		This command defines the contents of the currently selected output loss table. The table should contain an output loss
		for all measurement points. Each entry of the loss table consists of one measurement point and the corresponding loss.
		The table can contain up to 10001 entries. If you create a new table with this command, it will overwrite the current
		entries of the frequency list. \n
			:param frequency: Frequency of the measurement point. Range: 0 dB to 999.99 dB, Unit: HZ
			:param loss: Loss of the measurement point. Range: -999.99 dB to 999.99 dB, Unit: DB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle.as_open_list('frequency', frequency, DataType.FloatList, None), ArgSingle.as_open_list('loss', loss, DataType.FloatList, None))
		self._core.io.write(f'SENSe:CORRection:LOSS:OUTPut:TABLe:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Frequency: List[float]: Frequency of the measurement point. Range: 0 dB to 999.99 dB, Unit: HZ
			- Loss: List[float]: Loss of the measurement point. Range: -999.99 dB to 999.99 dB, Unit: DB"""
		__meta_args_list = [
			ArgStruct('Frequency', DataType.FloatList, None, False, True, 1),
			ArgStruct('Loss', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Frequency: List[float] = None
			self.Loss: List[float] = None

	def get(self) -> DataStruct:
		"""SCPI: [SENSe]:CORRection:LOSS:OUTPut:TABLe[:DATA] \n
		Snippet: value: DataStruct = driver.applications.k30NoiseFigure.sense.correction.loss.output.table.data.get() \n
		This command defines the contents of the currently selected output loss table. The table should contain an output loss
		for all measurement points. Each entry of the loss table consists of one measurement point and the corresponding loss.
		The table can contain up to 10001 entries. If you create a new table with this command, it will overwrite the current
		entries of the frequency list. \n
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:CORRection:LOSS:OUTPut:TABLe:DATA?', self.__class__.DataStruct())
