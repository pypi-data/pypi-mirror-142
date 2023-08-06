from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bottom:
	"""Bottom commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bottom", core, parent)

	def set(self, level: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:BOTTom \n
		Snippet: driver.applications.k30NoiseFigure.display.window.trace.y.scale.bottom.set(level = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the bottom value of the y-axis. \n
			:param level: The value ranges depend on the result display. Noise figure -75 dB to 75 dB Noise temperature -999990000 K to 999990000 K Y-factor -200 dB to 200 dB Gain -75 dB to 75 dB Power (hot) -200 dBm to 200 dBm Power (cold) -200 dBm to 200 dBm Unit: DB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:BOTTom {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:BOTTom \n
		Snippet: value: float = driver.applications.k30NoiseFigure.display.window.trace.y.scale.bottom.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the bottom value of the y-axis. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: level: The value ranges depend on the result display. Noise figure -75 dB to 75 dB Noise temperature -999990000 K to 999990000 K Y-factor -200 dB to 200 dB Gain -75 dB to 75 dB Power (hot) -200 dBm to 200 dBm Power (cold) -200 dBm to 200 dBm Unit: DB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:BOTTom?')
		return Conversions.str_to_float(response)
