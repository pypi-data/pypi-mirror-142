from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def copy(self, source_trace: enums.TraceTypeK30, target_trace: enums.TraceTypeK30, window=repcap.Window.Default) -> None:
		"""SCPI: TRACe<n>:COPY \n
		Snippet: driver.applications.k30NoiseFigure.trace.copy(source_trace = enums.TraceTypeK30.TRACe1, target_trace = enums.TraceTypeK30.TRACe1, window = repcap.Window.Default) \n
		This command copies data from one trace to another. \n
			:param source_trace: No help available
			:param target_trace: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('source_trace', source_trace, DataType.Enum, enums.TraceTypeK30), ArgSingle('target_trace', target_trace, DataType.Enum, enums.TraceTypeK30))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write_with_opc(f'TRACe{window_cmd_val}:COPY {param}'.rstrip())

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
