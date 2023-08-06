from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	def get(self, trace: enums.TraceTypeNumeric, window=repcap.Window.Default) -> str:
		"""SCPI: TRACe<n>[:DATA] \n
		Snippet: value: str = driver.applications.k18AmplifierEt.trace.data.get(trace = enums.TraceTypeNumeric.TRACe1, window = repcap.Window.Default) \n
		This command queries the measurement results in the graphical result displays. Usually, the measurement results are
		either displayed on the y-axis (two-dimensional diagrams) or the z-axis (three-dimensional diagrams) . \n
			:param trace: TRACE1 | ... | TRACE6 Selects the trace to be queried. Note that the available number of traces depends on the result display. For example, the Magnitude Capture result display only supports TRACE1, while the Time Domain result display supports TRACE1 to TRACE6.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: result: numeric value Values of the captured samples in chronological order."""
		param = Conversions.enum_scalar_to_str(trace, enums.TraceTypeNumeric)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:DATA? {param}')
		return trim_str_response(response)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
