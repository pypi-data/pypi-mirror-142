from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, freq_offset: List[float] = None, tolerance: List[float] = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:STATes[:DATA] \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.states.data.set(freq_offset = [1.1, 2.2, 3.3], tolerance = [1.1, 2.2, 3.3], window = repcap.Window.Default) \n
		This command sets and queries the hop state detection table. It consists of a comma-separated list of value pairs, one
		for each possible hop state. A maximum of 1000 states can be defined. Note that the state table can only be configured
		manually if method RsFsw.Applications.K60_Transient.Calculate.HopDetection.States.Auto.set is OFF. \n
			:param freq_offset: Frequency offsets from the center frequency Unit: HZ
			:param tolerance: Tolerance above or below the nominal frequency. Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('freq_offset', freq_offset, DataType.FloatList, None, True, True, 1), ArgSingle('tolerance', tolerance, DataType.FloatList, None, True, True, 1))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:STATes:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Freq_Offset: List[float]: Frequency offsets from the center frequency Unit: HZ
			- Tolerance: List[float]: Tolerance above or below the nominal frequency. Unit: HZ"""
		__meta_args_list = [
			ArgStruct('Freq_Offset', DataType.FloatList, None, False, True, 1),
			ArgStruct('Tolerance', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Freq_Offset: List[float] = None
			self.Tolerance: List[float] = None

	def get(self, window=repcap.Window.Default) -> DataStruct:
		"""SCPI: CALCulate<n>:HOPDetection:STATes[:DATA] \n
		Snippet: value: DataStruct = driver.applications.k60Transient.calculate.hopDetection.states.data.get(window = repcap.Window.Default) \n
		This command sets and queries the hop state detection table. It consists of a comma-separated list of value pairs, one
		for each possible hop state. A maximum of 1000 states can be defined. Note that the state table can only be configured
		manually if method RsFsw.Applications.K60_Transient.Calculate.HopDetection.States.Auto.set is OFF. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:STATes:DATA?', self.__class__.DataStruct())
