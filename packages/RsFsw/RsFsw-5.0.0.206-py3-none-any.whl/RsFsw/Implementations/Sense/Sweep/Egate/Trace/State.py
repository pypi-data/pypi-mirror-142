from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Status, default value after init: Status.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_status_get', 'repcap_status_set', repcap.Status.Nr1)

	def repcap_status_set(self, status: repcap.Status) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Status.Default
		Default value after init: Status.Nr1"""
		self._cmd_group.set_repcap_enum_value(status)

	def repcap_status_get(self) -> repcap.Status:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, state: bool, trace=repcap.Trace.Default, status=repcap.Status.Default) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>[:STATe<gr>] \n
		Snippet: driver.sense.sweep.egate.trace.state.set(state = False, trace = repcap.Trace.Default, status = repcap.Status.Default) \n
		This command includes or excludes a gate range for a particular trace. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:param status: optional repeated capability selector. Default value: Nr1 (settable in the interface 'State')
		"""
		param = Conversions.bool_to_str(state)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		status_cmd_val = self._cmd_group.get_repcap_cmd_value(status, repcap.Status)
		self._core.io.write(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:STATe{status_cmd_val} {param}')

	def get(self, trace=repcap.Trace.Default, status=repcap.Status.Default) -> bool:
		"""SCPI: [SENSe]:SWEep:EGATe:TRACe<t>[:STATe<gr>] \n
		Snippet: value: bool = driver.sense.sweep.egate.trace.state.get(trace = repcap.Trace.Default, status = repcap.Status.Default) \n
		This command includes or excludes a gate range for a particular trace. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:param status: optional repeated capability selector. Default value: Nr1 (settable in the interface 'State')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		status_cmd_val = self._cmd_group.get_repcap_cmd_value(status, repcap.Status)
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:TRACe{trace_cmd_val}:STATe{status_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
