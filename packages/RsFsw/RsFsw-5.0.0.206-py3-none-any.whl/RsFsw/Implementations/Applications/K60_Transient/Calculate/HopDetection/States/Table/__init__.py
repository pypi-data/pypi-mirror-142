from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 9 total commands, 7 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def replace(self):
		"""replace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_replace'):
			from .Replace import Replace
			self._replace = Replace(self._core, self._cmd_group)
		return self._replace

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	@property
	def nstates(self):
		"""nstates commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nstates'):
			from .Nstates import Nstates
			self._nstates = Nstates(self._core, self._cmd_group)
		return self._nstates

	@property
	def tolerance(self):
		"""tolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tolerance'):
			from .Tolerance import Tolerance
			self._tolerance = Tolerance(self._core, self._cmd_group)
		return self._tolerance

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	def load(self, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:STATes:TABLe:LOAD \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.states.table.load(filename = '1', window = repcap.Window.Default) \n
		Loads the signal state table configuration from the selected file. \n
			:param filename: String containing the path and name of the file.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(filename)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:STATes:TABLe:LOAD {param}')

	def save(self, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:STATes:TABLe:SAVE \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.states.table.save(filename = '1', window = repcap.Window.Default) \n
		Saves the current signal state table configuration to a file for later use. \n
			:param filename: String containing the path and name of the file.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(filename)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:STATes:TABLe:SAVE {param}')

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
