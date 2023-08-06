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

	def set(self, eval_type: enums.EvaluateType, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue] \n
		Snippet: driver.applications.k60Transient.calculate.trace.value.set(eval_type = enums.EvaluateType.ITIMe, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines which signal component (I/Q) is evaluated in which trace for the 'I/Q Time Domain' result display. This setting
		is not available for any other result displays. By default, the I component is displayed by trace 1, while the Q
		component is displayed by trace 4. \n
			:param eval_type: ITIMe | QTIMe ITIMe The I component is evaluated by the selected trace. QTIMe The Q component is evaluated by the selected trace.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(eval_type, enums.EvaluateType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.EvaluateType:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue] \n
		Snippet: value: enums.EvaluateType = driver.applications.k60Transient.calculate.trace.value.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines which signal component (I/Q) is evaluated in which trace for the 'I/Q Time Domain' result display. This setting
		is not available for any other result displays. By default, the I component is displayed by trace 1, while the Q
		component is displayed by trace 4. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: eval_type: ITIMe | QTIMe ITIMe The I component is evaluated by the selected trace. QTIMe The Q component is evaluated by the selected trace."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.EvaluateType)
