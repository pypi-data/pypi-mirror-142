from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:AUTO \n
		Snippet: driver.applications.k30NoiseFigure.display.window.trace.y.scale.auto.set(state = False, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command turns automatic scaling of the y-axis on and off. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:AUTO {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:Y[:SCALe]:AUTO \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.display.window.trace.y.scale.auto.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command turns automatic scaling of the y-axis on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:Y:SCALe:AUTO?')
		return Conversions.str_to_bool(response)
