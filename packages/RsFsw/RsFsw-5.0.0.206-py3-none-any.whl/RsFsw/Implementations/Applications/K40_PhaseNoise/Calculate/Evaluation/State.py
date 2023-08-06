from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:EVALuation[:STATe] \n
		Snippet: driver.applications.k40PhaseNoise.calculate.evaluation.state.set(state = False, window = repcap.Window.Default) \n
		This command turn integration of the measurement range for residual noise calculation on and off. \n
			:param state: OFF | 0 Calculates the residual noise over the entire measurement range. ON | 1 Calculates the residual noise over a customized range.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:EVALuation:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:EVALuation[:STATe] \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.calculate.evaluation.state.get(window = repcap.Window.Default) \n
		This command turn integration of the measurement range for residual noise calculation on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: OFF | 0 Calculates the residual noise over the entire measurement range. ON | 1 Calculates the residual noise over a customized range."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:EVALuation:STATe?')
		return Conversions.str_to_bool(response)
