from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ddpd:
	"""Ddpd commands group definition. 15 total commands, 10 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddpd", core, parent)

	@property
	def window(self):
		"""window commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def apply(self):
		"""apply commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def rms(self):
		"""rms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import Rms
			self._rms = Rms(self._core, self._cmd_group)
		return self._rms

	@property
	def finish(self):
		"""finish commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_finish'):
			from .Finish import Finish
			self._finish = Finish(self._core, self._cmd_group)
		return self._finish

	@property
	def fname(self):
		"""fname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fname'):
			from .Fname import Fname
			self._fname = Fname(self._core, self._cmd_group)
		return self._fname

	@property
	def fsave(self):
		"""fsave commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fsave'):
			from .Fsave import Fsave
			self._fsave = Fsave(self._core, self._cmd_group)
		return self._fsave

	@property
	def gexpansion(self):
		"""gexpansion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gexpansion'):
			from .Gexpansion import Gexpansion
			self._gexpansion = Gexpansion(self._core, self._cmd_group)
		return self._gexpansion

	@property
	def tradeoff(self):
		"""tradeoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tradeoff'):
			from .Tradeoff import Tradeoff
			self._tradeoff = Tradeoff(self._core, self._cmd_group)
		return self._tradeoff

	def continue_py(self) -> None:
		"""SCPI: CONFigure:DDPD:CONTinue \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.continue_py() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:DDPD:CONTinue')

	def continue_py_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DDPD:CONTinue \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.continue_py_with_opc() \n
		No command help available \n
		Same as continue_py, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DDPD:CONTinue', opc_timeout_ms)

	def abort(self) -> None:
		"""SCPI: CONFigure:DDPD:ABORt \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.abort() \n
		This command stops a DPD sequence and discards the predistorted I/Q data that have been calculated.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Initiate a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
		"""
		self._core.io.write(f'CONFigure:DDPD:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DDPD:ABORt \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.abort_with_opc() \n
		This command stops a DPD sequence and discards the predistorted I/Q data that have been calculated.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Initiate a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DDPD:ABORt', opc_timeout_ms)

	def start(self) -> None:
		"""SCPI: CONFigure:DDPD:STARt \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.start() \n
		This command initiates a direct DPD sequence with the number of iterations you have defined. You can define the number of
		iterations with method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.Count.set.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:DDPD:STARt')

	def start_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DDPD:STARt \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.start_with_opc() \n
		This command initiates a direct DPD sequence with the number of iterations you have defined. You can define the number of
		iterations with method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.Count.set.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DDPD:STARt', opc_timeout_ms)

	def clone(self) -> 'Ddpd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ddpd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
