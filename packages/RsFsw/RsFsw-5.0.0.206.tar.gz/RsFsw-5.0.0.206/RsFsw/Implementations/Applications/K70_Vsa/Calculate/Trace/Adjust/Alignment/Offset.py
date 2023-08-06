from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, fit_offset: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>:ADJust:ALIGnment:OFFSet \n
		Snippet: driver.applications.k70Vsa.calculate.trace.adjust.alignment.offset.set(fit_offset = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param fit_offset: Unit: SYM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(fit_offset)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:ADJust:ALIGnment:OFFSet {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: CALCulate<n>:TRACe<t>:ADJust:ALIGnment:OFFSet \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.trace.adjust.alignment.offset.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: fit_offset: Unit: SYM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:ADJust:ALIGnment:OFFSet?')
		return Conversions.str_to_float(response)
