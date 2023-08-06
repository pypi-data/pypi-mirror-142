from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 2 total commands, 1 Subgroups, 1 group commands
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

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import Relative
			self._relative = Relative(self._core, self._cmd_group)
		return self._relative

	def get(self, meas_type: enums.AdemMeasType, window=repcap.Window.Default, marker=repcap.Marker.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:ADEMod:ACV[:RESult<t>] \n
		Snippet: value: float = driver.calculate.marker.function.ademod.acv.result.get(meas_type = enums.AdemMeasType.MIDDle, window = repcap.Window.Default, marker = repcap.Marker.Default, trace = repcap.Trace.Default) \n
		No command help available \n
			:param meas_type: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Result')
			:return: meas_type_result: No help available"""
		param = Conversions.enum_scalar_to_str(meas_type, enums.AdemMeasType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:ADEMod:ACV:RESult{trace_cmd_val}? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
