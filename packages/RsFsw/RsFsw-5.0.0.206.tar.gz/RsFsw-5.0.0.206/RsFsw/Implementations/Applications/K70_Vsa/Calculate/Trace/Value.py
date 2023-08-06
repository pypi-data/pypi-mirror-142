from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, trace_ref_type: enums.TraceRefType, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.trace.value.set(trace_ref_type = enums.TraceRefType.ERRor, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This commands selects the signal to be used as the data source for a trace. For method RsFsw.Display.Window.Trace.Mode.
		set View, the data source to be evaluated cannot be changed. It remains set to the value that was most recently set. \n
			:param trace_ref_type: MEAS | REF | ERRor | TCAP MEAS Measurement signal REF Reference signal ERR Error TCAP Capture buffer
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(trace_ref_type, enums.TraceRefType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.TraceRefType:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue] \n
		Snippet: value: enums.TraceRefType = driver.applications.k70Vsa.calculate.trace.value.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This commands selects the signal to be used as the data source for a trace. For method RsFsw.Display.Window.Trace.Mode.
		set View, the data source to be evaluated cannot be changed. It remains set to the value that was most recently set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: trace_ref_type: MEAS | REF | ERRor | TCAP MEAS Measurement signal REF Reference signal ERR Error TCAP Capture buffer"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.TraceRefType)
