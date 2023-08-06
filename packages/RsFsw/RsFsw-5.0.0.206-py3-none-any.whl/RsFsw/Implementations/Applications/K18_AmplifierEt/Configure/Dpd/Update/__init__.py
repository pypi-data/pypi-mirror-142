from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Update:
	"""Update commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("update", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self) -> None:
		"""SCPI: CONFigure:DPD:UPDate \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.update.set() \n
		This command updates the DPD shaping tables on the R&S SMW when new measurement data is available.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:DPD:UPDate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DPD:UPDate \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.update.set_with_opc() \n
		This command updates the DPD shaping tables on the R&S SMW when new measurement data is available.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DPD:UPDate', opc_timeout_ms)

	def clone(self) -> 'Update':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Update(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
