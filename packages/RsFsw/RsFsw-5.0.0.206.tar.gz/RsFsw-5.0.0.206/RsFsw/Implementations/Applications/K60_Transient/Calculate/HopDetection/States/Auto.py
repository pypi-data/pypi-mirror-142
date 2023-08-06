from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:STATes:AUTO \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.states.auto.set(state = False, window = repcap.Window.Default) \n
		This command activates and deactivates the auto hop state detection. If deactivated, the states defined using method
		RsFsw.Applications.K60_Transient.Calculate.HopDetection.States.Data.set are used. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:STATes:AUTO {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:HOPDetection:STATes:AUTO \n
		Snippet: value: bool = driver.applications.k60Transient.calculate.hopDetection.states.auto.get(window = repcap.Window.Default) \n
		This command activates and deactivates the auto hop state detection. If deactivated, the states defined using method
		RsFsw.Applications.K60_Transient.Calculate.HopDetection.States.Data.set are used. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:STATes:AUTO?')
		return Conversions.str_to_bool(response)
