from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def piaq(self):
		"""piaq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_piaq'):
			from .Piaq import Piaq
			self._piaq = Piaq(self._core, self._cmd_group)
		return self._piaq

	def set(self, detector: enums.EvaluateType, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue] \n
		Snippet: driver.applications.k6Pulse.calculate.trace.value.set(detector = enums.EvaluateType.ITIMe, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines which signal component (I/Q) is evaluated in which trace for the 'Pulse I and Q' result display. This setting is
		not available for any other result displays. By default, the I component is displayed by trace 1, while the Q component
		is displayed by trace 4. \n
			:param detector: ITIMe | QTIMe ITIMe The I component is evaluated by the selected trace. QTIMe The Q component is evaluated by the selected trace.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(detector, enums.EvaluateType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.EvaluateType:
		"""SCPI: CALCulate<n>:TRACe<t>[:VALue] \n
		Snippet: value: enums.EvaluateType = driver.applications.k6Pulse.calculate.trace.value.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines which signal component (I/Q) is evaluated in which trace for the 'Pulse I and Q' result display. This setting is
		not available for any other result displays. By default, the I component is displayed by trace 1, while the Q component
		is displayed by trace 4. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: detector: ITIMe | QTIMe ITIMe The I component is evaluated by the selected trace. QTIMe The Q component is evaluated by the selected trace."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRACe{trace_cmd_val}:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.EvaluateType)

	def clone(self) -> 'Value':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Value(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
