from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K6_Pulse:
	"""K6_Pulse commands group definition. 966 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k6_Pulse", core, parent)

	@property
	def layout(self):
		"""layout commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_layout'):
			from .Layout import Layout
			self._layout = Layout(self._core, self._cmd_group)
		return self._layout

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def calculate(self):
		"""calculate commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_calculate'):
			from .Calculate import Calculate
			self._calculate = Calculate(self._core, self._cmd_group)
		return self._calculate

	@property
	def unit(self):
		"""unit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	@property
	def formatPy(self):
		"""formatPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def initiate(self):
		"""initiate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_initiate'):
			from .Initiate import Initiate
			self._initiate = Initiate(self._core, self._cmd_group)
		return self._initiate

	@property
	def inputPy(self):
		"""inputPy commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def riq(self):
		"""riq commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_riq'):
			from .Riq import Riq
			self._riq = Riq(self._core, self._cmd_group)
		return self._riq

	@property
	def massMemory(self):
		"""massMemory commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_massMemory'):
			from .MassMemory import MassMemory
			self._massMemory = MassMemory(self._core, self._cmd_group)
		return self._massMemory

	@property
	def output(self):
		"""output commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def sense(self):
		"""sense commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_sense'):
			from .Sense import Sense
			self._sense = Sense(self._core, self._cmd_group)
		return self._sense

	@property
	def system(self):
		"""system commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .System import System
			self._system = System(self._core, self._cmd_group)
		return self._system

	@property
	def trigger(self):
		"""trigger commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def calibration(self):
		"""calibration commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	def clone(self) -> 'K6_Pulse':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = K6_Pulse(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
