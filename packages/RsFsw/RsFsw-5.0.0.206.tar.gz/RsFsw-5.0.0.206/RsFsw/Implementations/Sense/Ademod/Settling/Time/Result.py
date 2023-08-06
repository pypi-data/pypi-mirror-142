from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
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

	def get(self, trace=repcap.Trace.Default) -> float:
		"""SCPI: [SENSe]:ADEMod:SETTling:TIME:RESult<t> \n
		Snippet: value: float = driver.sense.ademod.settling.time.result.get(trace = repcap.Trace.Default) \n
		Returns the settling time after which the signal remains within a specified target corridor. The settling time is
		evaluated for the selected trace in each time domain window.
		The value is only determined for [SENSe:]ADEMod:SETTling:TIME:STATe ON. For details, see 'Settling time'. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Result')
			:return: time: Unit: s"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'SENSe:ADEMod:SETTling:TIME:RESult{trace_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
