from typing import List

from .Internal.Core import Core
from .Internal.InstrumentErrors import RsInstrException
from .Internal.CommandsGroup import CommandsGroup
from .Internal.VisaSession import VisaSession


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsFsw:
	"""8762 total commands, 24 Subgroups, 1 group commands"""
	_driver_options = "SupportedInstrModels = FSW/FSWP/FSV/FSVR/FSVA, SupportedIdnPatterns = FSW/FSWP/FSV/FSVA/FSVR, SimulationIdnString = Rohde&Schwarz*FSW85*100001*5.0.0.0206"

	def __init__(self, resource_name: str, id_query: bool = True, reset: bool = False, options: str = None, direct_session: object = None):
		"""Initializes new RsFsw session. \n
		Parameter options tokens examples:
			- ``Simulate=True`` - starts the session in simulation mode. Default: ``False``
			- ``SelectVisa=socket`` - uses no VISA implementation for socket connections - you do not need any VISA-C installation
			- ``SelectVisa=rs`` - forces usage of RohdeSchwarz Visa
			- ``SelectVisa=ivi`` - forces usage of National Instruments Visa
			- ``QueryInstrumentStatus = False`` - same as ``driver.utilities.instrument_status_checking = False``. Default: ``True``
			- ``WriteDelay = 20, ReadDelay = 5`` - Introduces delay of 20ms before each write and 5ms before each read. Default: ``0ms`` for both
			- ``OpcWaitMode = OpcQuery`` - mode for all the opc-synchronised write/reads. Other modes: StbPolling, StbPollingSlow, StbPollingSuperSlow. Default: ``StbPolling``
			- ``AddTermCharToWriteBinBLock = True`` - Adds one additional LF to the end of the binary data (some instruments require that). Default: ``False``
			- ``AssureWriteWithTermChar = True`` - Makes sure each command/query is terminated with termination character. Default: Interface dependent
			- ``TerminationCharacter = "\\r"`` - Sets the termination character for reading. Default: ``\\n`` (LineFeed or LF)
			- ``DataChunkSize = 10E3`` - Maximum size of one write/read segment. If transferred data is bigger, it is split to more segments. Default: ``1E6`` bytes
			- ``OpcTimeout = 10000`` - same as driver.utilities.opc_timeout = 10000. Default: ``30000ms``
			- ``VisaTimeout = 5000`` - same as driver.utilities.visa_timeout = 5000. Default: ``10000ms``
			- ``ViClearExeMode = Disabled`` - viClear() execution mode. Default: ``execute_on_all``
			- ``OpcQueryAfterWrite = True`` - same as driver.utilities.opc_query_after_write = True. Default: ``False``
			- ``StbInErrorCheck = False`` - if true, the driver checks errors with *STB? If false, it uses SYST:ERR?. Default: ``True``
			- ``LoggingMode = LoggingMode.On`` - Sets the logging status right from the start. Default: ``Off``
			- ``LoggingName = 'MyDevice'`` - Sets the name to represent the session in the log entries. Default: ``'resource_name'``
		:param resource_name: VISA resource name, e.g. 'TCPIP::192.168.2.1::INSTR'
		:param id_query: if True: the instrument's model name is verified against the models supported by the driver and eventually throws an exception.
		:param reset: Resets the instrument (sends *RST command) and clears its status sybsystem.
		:param options: string tokens alternating the driver settings.
		:param direct_session: Another driver object or pyVisa object to reuse the session instead of opening a new session."""
		self._core = Core(resource_name, id_query, reset, RsFsw._driver_options, options, direct_session)
		self._core.driver_version = '5.0.0.0206'
		self._options = options
		self._add_all_global_repcaps()
		self._custom_properties_init()
		self.utilities.default_instrument_setup()
		# noinspection PyTypeChecker
		self._cmd_group = CommandsGroup("ROOT", self._core, None)

	@classmethod
	def from_existing_session(cls, session: object, options: str = None) -> 'RsFsw':
		"""Creates a new RsFsw object with the entered 'session' reused. \n
		:param session: can be another driver or a direct pyvisa session.
		:param options: string tokens alternating the driver settings."""
		# noinspection PyTypeChecker
		return cls(None, False, False, options, session)

	def __str__(self) -> str:
		if self._core.io:
			return f"RsFsw session '{self._core.io.resource_name}'"
		else:
			return f"RsFsw with session closed"

	@staticmethod
	def assert_minimum_version(min_version: str) -> None:
		"""Asserts that the driver version fulfills the minimum required version you have entered.
		This way you make sure your installed driver is of the entered version or newer."""
		min_version_list = min_version.split('.')
		curr_version_list = '5.0.0.0206'.split('.')
		count_min = len(min_version_list)
		count_curr = len(curr_version_list)
		count = count_min if count_min < count_curr else count_curr
		for i in range(count):
			minimum = int(min_version_list[i])
			curr = int(curr_version_list[i])
			if curr > minimum:
				break
			if curr < minimum:
				raise RsInstrException(f"Assertion for minimum RsFsw version failed. Current version: '5.0.0.0206', minimum required version: '{min_version}'")
				
	@staticmethod
	def list_resources(expression: str = '?*::INSTR', visa_select: str = None) -> List[str]:
		"""Finds all the resources defined by the expression
			- '?*' - matches all the available instruments
			- 'USB::?*' - matches all the USB instruments
			- 'TCPIP::192?*' - matches all the LAN instruments with the IP address starting with 192
		:param expression: see the examples in the function
		:param visa_select: optional parameter selecting a specific VISA. Examples: '@ivi', '@rs'
		"""
		rm = VisaSession.get_resource_manager(visa_select)
		resources = rm.list_resources(expression)
		rm.close()
		# noinspection PyTypeChecker
		return resources

	def close(self) -> None:
		"""Closes the active RsFsw session."""
		self._core.io.close()

	def get_session_handle(self) -> object:
		"""Returns the underlying session handle."""
		return self._core.get_session_handle()

	def _add_all_global_repcaps(self) -> None:
		"""Adds all the repcaps defined as global to the instrument's global repcaps dictionary."""

	def _custom_properties_init(self):
		"""Adds all the interfaces that are custom for the driver."""
		from .CustomFiles.utilities import Utilities
		self.utilities = Utilities(self._core)
		from .CustomFiles.events import Events
		self.events = Events(self._core)

	@property
	def layout(self):
		"""layout commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_layout'):
			from .Implementations.Layout import Layout
			self._layout = Layout(self._core, self._cmd_group)
		return self._layout

	@property
	def massMemory(self):
		"""massMemory commands group. 14 Sub-classes, 3 commands."""
		if not hasattr(self, '_massMemory'):
			from .Implementations.MassMemory import MassMemory
			self._massMemory = MassMemory(self._core, self._cmd_group)
		return self._massMemory

	@property
	def sense(self):
		"""sense commands group. 28 Sub-classes, 0 commands."""
		if not hasattr(self, '_sense'):
			from .Implementations.Sense import Sense
			self._sense = Sense(self._core, self._cmd_group)
		return self._sense

	@property
	def calculate(self):
		"""calculate commands group. 22 Sub-classes, 0 commands."""
		if not hasattr(self, '_calculate'):
			from .Implementations.Calculate import Calculate
			self._calculate = Calculate(self._core, self._cmd_group)
		return self._calculate

	@property
	def instrument(self):
		"""instrument commands group. 8 Sub-classes, 2 commands."""
		if not hasattr(self, '_instrument'):
			from .Implementations.Instrument import Instrument
			self._instrument = Instrument(self._core, self._cmd_group)
		return self._instrument

	@property
	def trace(self):
		"""trace commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Implementations.Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def display(self):
		"""display commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_display'):
			from .Implementations.Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	@property
	def formatPy(self):
		"""formatPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_formatPy'):
			from .Implementations.FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def inputPy(self):
		"""inputPy commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .Implementations.InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def status(self):
		"""status commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_status'):
			from .Implementations.Status import Status
			self._status = Status(self._core, self._cmd_group)
		return self._status

	@property
	def applications(self):
		"""applications commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_applications'):
			from .Implementations.Applications import Applications
			self._applications = Applications(self._core, self._cmd_group)
		return self._applications

	@property
	def system(self):
		"""system commands group. 29 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .Implementations.System import System
			self._system = System(self._core, self._cmd_group)
		return self._system

	@property
	def calibration(self):
		"""calibration commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Implementations.Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def configure(self):
		"""configure commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Implementations.Configure import Configure
			self._configure = Configure(self._core, self._cmd_group)
		return self._configure

	@property
	def fetch(self):
		"""fetch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fetch'):
			from .Implementations.Fetch import Fetch
			self._fetch = Fetch(self._core, self._cmd_group)
		return self._fetch

	@property
	def initiate(self):
		"""initiate commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_initiate'):
			from .Implementations.Initiate import Initiate
			self._initiate = Initiate(self._core, self._cmd_group)
		return self._initiate

	@property
	def output(self):
		"""output commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Implementations.Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def read(self):
		"""read commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_read'):
			from .Implementations.Read import Read
			self._read = Read(self._core, self._cmd_group)
		return self._read

	@property
	def source(self):
		"""source commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_source'):
			from .Implementations.Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def trigger(self):
		"""trigger commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Implementations.Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def unit(self):
		"""unit commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Implementations.Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def hardCopy(self):
		"""hardCopy commands group. 14 Sub-classes, 1 commands."""
		if not hasattr(self, '_hardCopy'):
			from .Implementations.HardCopy import HardCopy
			self._hardCopy = HardCopy(self._core, self._cmd_group)
		return self._hardCopy

	@property
	def diagnostic(self):
		"""diagnostic commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_diagnostic'):
			from .Implementations.Diagnostic import Diagnostic
			self._diagnostic = Diagnostic(self._core, self._cmd_group)
		return self._diagnostic

	@property
	def triggerInvoke(self):
		"""triggerInvoke commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_triggerInvoke'):
			from .Implementations.TriggerInvoke import TriggerInvoke
			self._triggerInvoke = TriggerInvoke(self._core, self._cmd_group)
		return self._triggerInvoke

	def abort(self) -> None:
		"""SCPI: ABORt \n
		Snippet: driver.abort() \n
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
			- Visa: viClear
			- GPIB: ibclr
			- RSIB: RSDLLibclr
		Now you can send the [CMDLINKRESOLVED #Abort CMDLINKRESOLVED] command on the remote channel performing the measurement. \n
		"""
		self._core.io.write(f'ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt \n
		Snippet: driver.abort_with_opc() \n
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
			- Visa: viClear
			- GPIB: ibclr
			- RSIB: RSDLLibclr
		Now you can send the [CMDLINKRESOLVED #Abort CMDLINKRESOLVED] command on the remote channel performing the measurement. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt', opc_timeout_ms)

	def clone(self) -> 'RsFsw':
		"""Creates a deep copy of the RsFsw object. Also copies:
			- All the existing Global repeated capability values
			- All the default group repeated capabilities setting \n
		Does not check the *IDN? response, and does not perform Reset.
		After cloning, you can set all the repeated capabilities settings independentely from the original group.
		Calling close() on the new object does not close the original VISA session"""
		cloned = RsFsw.from_existing_session(self.get_session_handle(), self._options)
		self._cmd_group.synchronize_repcaps(cloned)
		
		return cloned

	def restore_all_repcaps_to_default(self) -> None:
		"""Sets all the Group and Global repcaps to their initial values"""
		self._cmd_group.restore_repcaps()
