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

	def set(self, state: bool, scaling: enums.TimeScaling = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:TABLe:PMSettling:ALL[:STATe] \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.table.pmSettling.all.state.set(state = False, scaling = enums.TimeScaling.MS, window = repcap.Window.Default) \n
		If enabled, all PM settling parameters are included in the result tables (see 'PM settling parameters') . Note that only
		the enabled columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Table.Results.
		get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param scaling: S | MS | US | NS Defines the scaling for the PM settling parameters
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('state', state, DataType.Boolean), ArgSingle('scaling', scaling, DataType.Enum, enums.TimeScaling, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:TABLe:PMSettling:ALL:STATe {param}'.rstrip())
