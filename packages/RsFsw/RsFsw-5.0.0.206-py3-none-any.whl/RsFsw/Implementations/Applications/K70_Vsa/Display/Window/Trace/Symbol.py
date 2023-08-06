from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbol:
	"""Symbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbol", core, parent)

	def set(self, symbols: enums.TraceSymbols, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:SYMBol \n
		Snippet: driver.applications.k70Vsa.display.window.trace.symbol.set(symbols = enums.TraceSymbols.BARS, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command enables the display of the decision instants (time when the signals occurred) as dots on the trace. \n
			:param symbols: ON | OFF | 0 | 1 OFF | 0 Symbols are displayed. ON | 1 Symbols are not displayed.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(symbols, enums.TraceSymbols)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:SYMBol {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.TraceSymbols:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:SYMBol \n
		Snippet: value: enums.TraceSymbols = driver.applications.k70Vsa.display.window.trace.symbol.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command enables the display of the decision instants (time when the signals occurred) as dots on the trace. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: symbols: ON | OFF | 0 | 1 OFF | 0 Symbols are displayed. ON | 1 Symbols are not displayed."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:SYMBol?')
		return Conversions.str_to_scalar_enum(response, enums.TraceSymbols)
