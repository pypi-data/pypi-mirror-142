from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hcontinuous:
	"""Hcontinuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hcontinuous", core, parent)

	def set(self, hold: bool, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:MODE:HCONtinuous \n
		Snippet: driver.display.window.trace.mode.hcontinuous.set(hold = False, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param hold: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.bool_to_str(hold)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:MODE:HCONtinuous {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:MODE:HCONtinuous \n
		Snippet: value: bool = driver.display.window.trace.mode.hcontinuous.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: hold: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:MODE:HCONtinuous?')
		return Conversions.str_to_bool(response)
