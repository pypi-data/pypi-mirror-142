from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Trace, default value after init: Trace.Tr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_trace_get', 'repcap_trace_set', repcap.Trace.Tr1)

	def repcap_trace_set(self, trace: repcap.Trace) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Trace.Default
		Default value after init: Trace.Tr1"""
		self._cmd_group.set_repcap_enum_value(trace)

	def repcap_trace_get(self) -> repcap.Trace:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, result_type: enums.ResultTypeB, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: CALCulate<n>:STATistics:RESult<res> \n
		Snippet: driver.applications.k91Wlan.calculate.statistics.result.set(result_type = enums.ResultTypeB.ALL, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command queries the results of a measurement for a specific trace. \n
			:param result_type: MEAN Average (=RMS) power in dBm measured during the measurement time. PEAK Peak power in dBm measured during the measurement time. CFACtor Determined crest factor (= ratio of peak power to average power) in dB. ALL Results of all three measurements mentioned before, separated by commas: mean power,peak power,crest factor
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Result')
		"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CALCulate{window_cmd_val}:STATistics:RESult{trace_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.ResultTypeB:
		"""SCPI: CALCulate<n>:STATistics:RESult<res> \n
		Snippet: value: enums.ResultTypeB = driver.applications.k91Wlan.calculate.statistics.result.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command queries the results of a measurement for a specific trace. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Result')
			:return: result_type: MEAN Average (=RMS) power in dBm measured during the measurement time. PEAK Peak power in dBm measured during the measurement time. CFACtor Determined crest factor (= ratio of peak power to average power) in dB. ALL Results of all three measurements mentioned before, separated by commas: mean power,peak power,crest factor"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:STATistics:RESult{trace_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.ResultTypeB)

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
