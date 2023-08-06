from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K40_PhaseNoise:
	"""K40_PhaseNoise commands group definition. 211 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k40_PhaseNoise", core, parent)

	@property
	def layout(self):
		"""layout commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_layout'):
			from .Layout import Layout
			self._layout = Layout(self._core, self._cmd_group)
		return self._layout

	@property
	def calculate(self):
		"""calculate commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_calculate'):
			from .Calculate import Calculate
			self._calculate = Calculate(self._core, self._cmd_group)
		return self._calculate

	@property
	def fetch(self):
		"""fetch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fetch'):
			from .Fetch import Fetch
			self._fetch = Fetch(self._core, self._cmd_group)
		return self._fetch

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def sense(self):
		"""sense commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_sense'):
			from .Sense import Sense
			self._sense = Sense(self._core, self._cmd_group)
		return self._sense

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	@property
	def configure(self):
		"""configure commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import Configure
			self._configure = Configure(self._core, self._cmd_group)
		return self._configure

	@property
	def formatPy(self):
		"""formatPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def initiate(self):
		"""initiate commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_initiate'):
			from .Initiate import Initiate
			self._initiate = Initiate(self._core, self._cmd_group)
		return self._initiate

	@property
	def inputPy(self):
		"""inputPy commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def massMemory(self):
		"""massMemory commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_massMemory'):
			from .MassMemory import MassMemory
			self._massMemory = MassMemory(self._core, self._cmd_group)
		return self._massMemory

	@property
	def output(self):
		"""output commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def triggerInvoke(self):
		"""triggerInvoke commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_triggerInvoke'):
			from .TriggerInvoke import TriggerInvoke
			self._triggerInvoke = TriggerInvoke(self._core, self._cmd_group)
		return self._triggerInvoke

	def clone(self) -> 'K40_PhaseNoise':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = K40_PhaseNoise(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
