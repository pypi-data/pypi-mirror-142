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
class RmsFm:
	"""RmsFm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmsFm", core, parent)

	def set(self, state: bool, scaling: enums.FrequencyScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:RMSFm \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.frequency.rmsFm.set(state = False, scaling = enums.FrequencyScaling.GHZ, window = repcap.Window.Default) \n
		If enabled, the specified frequency parameter is included in the result tables (see 'Frequency parameters') . Note that
		only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Table.
		Results.get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			:param scaling: GHZ | MHZ | KHZ | HZ Defines the scaling for the frequency parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.FrequencyScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:RMSFm {param}'.rstrip())

	# noinspection PyTypeChecker
	class RmsFmStruct(StructBase):
		"""Response structure. Fields: \n
			- State: bool: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			- Scaling: enums.FrequencyScaling: GHZ | MHZ | KHZ | HZ Defines the scaling for the frequency parameters"""
		__meta_args_list = [
			ArgStruct.scalar_bool('State'),
			ArgStruct.scalar_enum('Scaling', enums.FrequencyScaling)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.State: bool = None
			self.Scaling: enums.FrequencyScaling = None

	def get(self, window=repcap.Window.Default) -> RmsFmStruct:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:RMSFm \n
		Snippet: value: RmsFmStruct = driver.applications.k60Transient.calculate.chrDetection.table.frequency.rmsFm.get(window = repcap.Window.Default) \n
		If enabled, the specified frequency parameter is included in the result tables (see 'Frequency parameters') . Note that
		only the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Table.
		Results.get_ query. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for RmsFmStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:RMSFm?', self.__class__.RmsFmStruct())
