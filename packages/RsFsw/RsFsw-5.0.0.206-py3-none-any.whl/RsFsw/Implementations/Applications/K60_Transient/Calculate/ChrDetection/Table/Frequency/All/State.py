from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, visability: bool, scaling: enums.FrequencyScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:FREQuency:ALL[:STATe] \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.frequency.all.state.set(visability = False, scaling = enums.FrequencyScaling.GHZ, window = repcap.Window.Default) \n
		If enabled, all frequency parameters are included in the result tables (see 'Frequency parameters') . Note that only the
		enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Table.Results.
		get_ query. \n
			:param visability: No help available
			:param scaling: GHZ | MHZ | KHZ | HZ Defines the scaling for the frequency parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('visability', visability, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.FrequencyScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:FREQuency:ALL:STATe {param}'.rstrip())
