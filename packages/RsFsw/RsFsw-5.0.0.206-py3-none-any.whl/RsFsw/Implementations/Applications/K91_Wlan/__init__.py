from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class K91_Wlan:
	"""K91_Wlan commands group definition. 511 total commands, 17 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("k91_Wlan", core, parent)

	@property
	def layout(self):
		"""layout commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_layout'):
			from .Layout import Layout
			self._layout = Layout(self._core, self._cmd_group)
		return self._layout

	@property
	def massMemory(self):
		"""massMemory commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_massMemory'):
			from .MassMemory import MassMemory
			self._massMemory = MassMemory(self._core, self._cmd_group)
		return self._massMemory

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def configure(self):
		"""configure commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import Configure
			self._configure = Configure(self._core, self._cmd_group)
		return self._configure

	@property
	def calculate(self):
		"""calculate commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_calculate'):
			from .Calculate import Calculate
			self._calculate = Calculate(self._core, self._cmd_group)
		return self._calculate

	@property
	def fetch(self):
		"""fetch commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_fetch'):
			from .Fetch import Fetch
			self._fetch = Fetch(self._core, self._cmd_group)
		return self._fetch

	@property
	def sense(self):
		"""sense commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_sense'):
			from .Sense import Sense
			self._sense = Sense(self._core, self._cmd_group)
		return self._sense

	@property
	def calibration(self):
		"""calibration commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def display(self):
		"""display commands group. 2 Sub-classes, 0 commands."""
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
		"""initiate commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_initiate'):
			from .Initiate import Initiate
			self._initiate = Initiate(self._core, self._cmd_group)
		return self._initiate

	@property
	def inputPy(self):
		"""inputPy commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def output(self):
		"""output commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def system(self):
		"""system commands group. 1 Sub-classes, 0 commands."""
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
	def triggerInvoke(self):
		"""triggerInvoke commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_triggerInvoke'):
			from .TriggerInvoke import TriggerInvoke
			self._triggerInvoke = TriggerInvoke(self._core, self._cmd_group)
		return self._triggerInvoke

	@property
	def unit(self):
		"""unit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def abort(self) -> None:
		"""SCPI: ABORt \n
		Snippet: driver.applications.k91_Wlan.abort() \n
		This command aborts the measurement in the current channel and resets the trigger system. To prevent overlapping
		execution of the subsequent command before the measurement has been aborted successfully, use the *OPC? or *WAI command
		after method RsFsw.#Abort CMDLINKRESOLVED] and before the next command. For details on overlapping execution see Remote
		control via SCPI. To abort a sequence of measurements by the Sequencer, use the [CMDLINKRESOLVED Initiate.Sequencer.abort
		command. Note on blocked remote control programs: If a sequential command cannot be completed, for example because a
		triggered sweep never receives a trigger, the remote control program will never finish and the remote channel to the R&S
		FSW is blocked for further commands. In this case, you must interrupt processing on the remote channel first in order to
		abort the measurement. To do so, send a 'Device Clear' command from the control instrument to the R&S FSW on a parallel
		channel to clear all currently active remote channels. Depending on the used interface and protocol, send the following
		commands:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Visa: viClear
			- GPIB: ibclr
			- RSIB: RSDLLibclr
		Now you can send the [CMDLINKRESOLVED #Abort CMDLINKRESOLVED] command on the remote channel performing the measurement. \n
		"""
		self._core.io.write(f'ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt \n
		Snippet: driver.applications.k91_Wlan.abort_with_opc() \n
		This command aborts the measurement in the current channel and resets the trigger system. To prevent overlapping
		execution of the subsequent command before the measurement has been aborted successfully, use the *OPC? or *WAI command
		after method RsFsw.#Abort CMDLINKRESOLVED] and before the next command. For details on overlapping execution see Remote
		control via SCPI. To abort a sequence of measurements by the Sequencer, use the [CMDLINKRESOLVED Initiate.Sequencer.abort
		command. Note on blocked remote control programs: If a sequential command cannot be completed, for example because a
		triggered sweep never receives a trigger, the remote control program will never finish and the remote channel to the R&S
		FSW is blocked for further commands. In this case, you must interrupt processing on the remote channel first in order to
		abort the measurement. To do so, send a 'Device Clear' command from the control instrument to the R&S FSW on a parallel
		channel to clear all currently active remote channels. Depending on the used interface and protocol, send the following
		commands:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Visa: viClear
			- GPIB: ibclr
			- RSIB: RSDLLibclr
		Now you can send the [CMDLINKRESOLVED #Abort CMDLINKRESOLVED] command on the remote channel performing the measurement. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt', opc_timeout_ms)

	def clone(self) -> 'K91_Wlan':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = K91_Wlan(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
