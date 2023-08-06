from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> int:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:STOP \n
		Snippet: value: int = driver.applications.k70Vsa.display.window.trace.x.scale.stop.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command queries the last value of the x-axis in the specified window in symbols or time, depending on the unit
		setting for the x-axis. Note: If the burst is shifted (using the CALC:TRAC:ALIG commands) the x-axis no longer begins at
		0 symbols on the left, but at a user-defined value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: stop: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:STOP?')
		return Conversions.str_to_int(response)
