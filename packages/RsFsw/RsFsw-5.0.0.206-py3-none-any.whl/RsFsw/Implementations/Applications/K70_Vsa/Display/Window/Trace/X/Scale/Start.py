from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> int:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:STARt \n
		Snippet: value: int = driver.applications.k70Vsa.display.window.trace.x.scale.start.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command queries the first value of the x-axis in the specified window in symbols or time, depending on the unit
		setting for the x-axis. Note: using the method RsFsw.Applications.K70_Vsa.Calculate.Trace.Adjust.Alignment.Offset.
		set command, the burst is shifted in the diagram; the x-axis thus no longer begins on the left at 0 symbols but at a
		selectable value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: start: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:STARt?')
		return Conversions.str_to_int(response)
