from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:POWer:ALL[:STATe] \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.power.all.state.set(state = False, window = repcap.Window.Default) \n
		If enabled, all power parameters are included in the result tables (see 'Power parameters') . Note that only the enabled
		columns are returned for the method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Table.Results.get_ query. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:POWer:ALL:STATe {param}')
