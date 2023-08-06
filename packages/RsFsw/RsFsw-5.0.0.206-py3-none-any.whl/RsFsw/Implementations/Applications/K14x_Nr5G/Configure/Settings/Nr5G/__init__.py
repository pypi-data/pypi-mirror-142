from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5G:
	"""Nr5G commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	@property
	def pinterval(self):
		"""pinterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pinterval'):
			from .Pinterval import Pinterval
			self._pinterval = Pinterval(self._core, self._cmd_group)
		return self._pinterval

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	def set(self) -> None:
		"""SCPI: CONFigure:SETTings:NR5G \n
		Snippet: driver.applications.k14Xnr5G.configure.settings.nr5G.set() \n
		This command downloads the NR signal description from the generator to the analyzer.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:SETTings:NR5G')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:SETTings:NR5G \n
		Snippet: driver.applications.k14Xnr5G.configure.settings.nr5G.set_with_opc() \n
		This command downloads the NR signal description from the generator to the analyzer.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- IP connection to a signal generator.
			- Generator control state is on (method RsFsw.Applications.K18_AmplifierEt.Configure.Generator.Control.State.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:SETTings:NR5G', opc_timeout_ms)

	def clone(self) -> 'Nr5G':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nr5G(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
