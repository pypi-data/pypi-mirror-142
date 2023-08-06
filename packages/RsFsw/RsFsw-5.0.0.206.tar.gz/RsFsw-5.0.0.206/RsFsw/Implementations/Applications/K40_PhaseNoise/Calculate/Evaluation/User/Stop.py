from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, offset_frequency: float, window=repcap.Window.Default, userRange=repcap.UserRange.Default) -> None:
		"""SCPI: CALCulate<n>:EVALuation:USER<res>:STOP \n
		Snippet: driver.applications.k40PhaseNoise.calculate.evaluation.user.stop.set(offset_frequency = 1.0, window = repcap.Window.Default, userRange = repcap.UserRange.Default) \n
		This command defines the end point of a custom residual noise calculation range. Before you can use the command, you have
		to assign the user range to a trace with method RsFsw.Applications.K40_PhaseNoise.Calculate.Evaluation.User.Trace.set. \n
			:param offset_frequency: The minimum offset is 1 Hz. The maximum offset depends on the hardware you are using. Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param userRange: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(offset_frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		userRange_cmd_val = self._cmd_group.get_repcap_cmd_value(userRange, repcap.UserRange)
		self._core.io.write(f'CALCulate{window_cmd_val}:EVALuation:USER{userRange_cmd_val}:STOP {param}')

	def get(self, window=repcap.Window.Default, userRange=repcap.UserRange.Default) -> float:
		"""SCPI: CALCulate<n>:EVALuation:USER<res>:STOP \n
		Snippet: value: float = driver.applications.k40PhaseNoise.calculate.evaluation.user.stop.get(window = repcap.Window.Default, userRange = repcap.UserRange.Default) \n
		This command defines the end point of a custom residual noise calculation range. Before you can use the command, you have
		to assign the user range to a trace with method RsFsw.Applications.K40_PhaseNoise.Calculate.Evaluation.User.Trace.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param userRange: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: offset_frequency: The minimum offset is 1 Hz. The maximum offset depends on the hardware you are using. Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		userRange_cmd_val = self._cmd_group.get_repcap_cmd_value(userRange, repcap.UserRange)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:EVALuation:USER{userRange_cmd_val}:STOP?')
		return Conversions.str_to_float(response)
