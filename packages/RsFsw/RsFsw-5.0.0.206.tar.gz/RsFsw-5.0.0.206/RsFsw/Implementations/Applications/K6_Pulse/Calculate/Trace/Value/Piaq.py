from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Piaq:
	"""Piaq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("piaq", core, parent)

	def set(self, detector: enums.EvaluateType, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue]:PIAQ \n
		Snippet: driver.applications.k6Pulse.calculate.trace.value.piaq.set(detector = enums.EvaluateType.ITIMe, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines which signal component (I/Q) is evaluated in which trace for the 'Pulse I and Q' result display. By default, the
		I component is displayed by trace 1, while the Q component is displayed by trace 4. This setting is not available for any
		other results displays. \n
			:param detector: ITIMe | QTIMe ITIMe The I component is evaluated by the selected trace. QTIMe The Q component is evaluated by the selected trace.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.EvaluateType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue:PIAQ {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.EvaluateType:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue]:PIAQ \n
		Snippet: value: enums.EvaluateType = driver.applications.k6Pulse.calculate.trace.value.piaq.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines which signal component (I/Q) is evaluated in which trace for the 'Pulse I and Q' result display. By default, the
		I component is displayed by trace 1, while the Q component is displayed by trace 4. This setting is not available for any
		other results displays. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: detector: ITIMe | QTIMe ITIMe The I component is evaluated by the selected trace. QTIMe The Q component is evaluated by the selected trace."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue:PIAQ?')
		return Conversions.str_to_scalar_enum(response, enums.EvaluateType)
