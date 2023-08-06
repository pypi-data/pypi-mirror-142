from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaxPower:
	"""MaxPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maxPower", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:POWer:MAXPower \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.table.power.maxPower.set(state = False, window = repcap.Window.Default) \n
		No command help available \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:POWer:MAXPower {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:HOPDetection:TABLe:POWer:MAXPower \n
		Snippet: value: bool = driver.applications.k60Transient.calculate.hopDetection.table.power.maxPower.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 0 | 1 OFF | 0 The parameter is included. ON | 1 The parameter is not included"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:TABLe:POWer:MAXPower?')
		return Conversions.str_to_bool(response)
