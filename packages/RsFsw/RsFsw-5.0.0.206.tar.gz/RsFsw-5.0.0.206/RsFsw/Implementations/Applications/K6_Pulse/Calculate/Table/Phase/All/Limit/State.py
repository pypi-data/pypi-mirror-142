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
		"""SCPI: CALCulate<n>:TABLe:PHASe:ALL:LIMit:STATe \n
		Snippet: driver.applications.k6Pulse.calculate.table.phase.all.limit.state.set(state = False, window = repcap.Window.Default) \n
		Activates or deactivates a limit check for all parameters in the selected parameter group. Commands for the parameter
		group <TSIDelobe> are only available if the additional option R&S FSW-K6S is installed. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TABLe:PHASe:ALL:LIMit:STATe {param}')
