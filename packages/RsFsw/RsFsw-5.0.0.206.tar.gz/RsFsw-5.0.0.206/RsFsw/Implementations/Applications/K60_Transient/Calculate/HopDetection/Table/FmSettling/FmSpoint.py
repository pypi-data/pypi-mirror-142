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
class FmSpoint:
	"""FmSpoint commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmSpoint", core, parent)

	def set(self, state: bool, scaling: enums.TimeScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:FMSettling:FMSPoint \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.fmSettling.fmSpoint.set(state = False, scaling = enums.TimeScaling.MS, window = repcap.Window.Default) \n
		If enabled, the specified FM settling parameter is included in the result tables (see 'FM settling parameters') .
		Note that only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.
		Table.Results.get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param scaling: S | MS | US | NS Defines the scaling for the FM settling parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.TimeScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:FMSettling:FMSPoint {param}'.rstrip())

	# noinspection PyTypeChecker
	class FmSpointStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			- Scaling: enums.TimeScaling: S | MS | US | NS Defines the scaling for the FM settling parameters"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.TimeScaling)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.TimeScaling = None

	def get(self, window=repcap.Window.Default) -> FmSpointStruct:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:FMSettling:FMSPoint \n
		Snippet: value: FmSpointStruct = driver.applications.k60Transient.calculate.hopDetection.table.fmSettling.fmSpoint.get(window = repcap.Window.Default) \n
		If enabled, the specified FM settling parameter is included in the result tables (see 'FM settling parameters') .
		Note that only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.
		Table.Results.get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for FmSpointStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:FMSettling:FMSPoint?', self.__class__.FmSpointStruct())
