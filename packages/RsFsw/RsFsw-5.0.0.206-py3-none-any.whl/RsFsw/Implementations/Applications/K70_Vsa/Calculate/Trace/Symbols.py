from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbols:
	"""Symbols commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbols", core, parent)

	def set(self, symbol_selection: enums.SymbolSelection, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>:SYMBols \n
		Snippet: driver.applications.k70Vsa.calculate.trace.symbols.set(symbol_selection = enums.SymbolSelection.ALL, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This commands selects which symbols are displayed by a trace (in a constellation graph with 2 modulations) . For method
		RsFsw.Display.Window.Trace.Mode.set View, the symbol selection cannot be changed. It remains set to the value that was
		most recently set. \n
			:param symbol_selection: ALL | PATTern | DATA ALL Trace consists of constellation points for all symbols PATTern Trace consists of only pattern symbols DATA Trace consists of only data symbols
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(symbol_selection, enums.SymbolSelection)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:SYMBols {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.SymbolSelection:
		"""SCPI: CALCulate<n>:TRACe<t>:SYMBols \n
		Snippet: value: enums.SymbolSelection = driver.applications.k70Vsa.calculate.trace.symbols.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This commands selects which symbols are displayed by a trace (in a constellation graph with 2 modulations) . For method
		RsFsw.Display.Window.Trace.Mode.set View, the symbol selection cannot be changed. It remains set to the value that was
		most recently set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: symbol_selection: ALL | PATTern | DATA ALL Trace consists of constellation points for all symbols PATTern Trace consists of only pattern symbols DATA Trace consists of only data symbols"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:SYMBols?')
		return Conversions.str_to_scalar_enum(response, enums.SymbolSelection)
