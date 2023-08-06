from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, reference: enums.TraceReference, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>:ADJust[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.trace.adjust.value.set(reference = enums.TraceReference.BURSt, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the reference point for the display. \n
			:param reference: TRIGger | BURSt | PATTern TRIGger The reference point is defined by the start of the capture buffer. BURSt The reference point is defined by the start/center/end of the burst. PATTern The instrument selects the reference point and the alignment.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.TraceReference)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:ADJust:VALue {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.TraceReference:
		"""SCPI: CALCulate<n>:TRACe<t>:ADJust[:VALue] \n
		Snippet: value: enums.TraceReference = driver.applications.k70Vsa.calculate.trace.adjust.value.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command defines the reference point for the display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: reference: TRIGger | BURSt | PATTern TRIGger The reference point is defined by the start of the capture buffer. BURSt The reference point is defined by the start/center/end of the burst. PATTern The instrument selects the reference point and the alignment."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:ADJust:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.TraceReference)
