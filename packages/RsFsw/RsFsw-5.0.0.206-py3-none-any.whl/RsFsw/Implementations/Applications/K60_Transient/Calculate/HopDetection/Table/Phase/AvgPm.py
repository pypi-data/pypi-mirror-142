from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AvgPm:
	"""AvgPm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("avgPm", core, parent)

	def set(self, state: bool, scaling: enums.AngleUnit = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:PHASe:AVGPm \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.phase.avgPm.set(state = False, scaling = enums.AngleUnit.DEG, window = repcap.Window.Default) \n
		If enabled, the specified phase deviation parameter is included in the result tables (see 'Phase parameters') . Note that
		only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.
		Results.get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			:param scaling: DEG | RAD Defines the scaling for the phase parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.AngleUnit, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:PHASe:AVGPm {param}'.rstrip())

	# noinspection PyTypeChecker
	class AvgPmStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			- Scaling: enums.AngleUnit: DEG | RAD Defines the scaling for the phase parameters"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.AngleUnit)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.AngleUnit = None

	def get(self, window=repcap.Window.Default) -> AvgPmStruct:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:PHASe:AVGPm \n
		Snippet: value: AvgPmStruct = driver.applications.k60Transient.calculate.hopDetection.table.phase.avgPm.get(window = repcap.Window.Default) \n
		If enabled, the specified phase deviation parameter is included in the result tables (see 'Phase parameters') . Note that
		only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.
		Results.get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for AvgPmStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:PHASe:AVGPm?', self.__class__.AvgPmStruct())
