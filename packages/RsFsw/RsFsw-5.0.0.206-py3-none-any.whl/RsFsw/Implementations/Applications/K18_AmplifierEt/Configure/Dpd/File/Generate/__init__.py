from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generate:
	"""Generate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generate", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def set(self) -> None:
		"""SCPI: CONFigure:DPD:FILE:GENerate \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.file.generate.set() \n
		This command generates the waveform files containing predistortion information within the amplifier application. All in
		all, the command generates three waveform files: AM/AM only, AM/PM only and AM/AM plus AM/PM. It also transfers these
		waveform files to the connected signal generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:DPD:FILE:GENerate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DPD:FILE:GENerate \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.file.generate.set_with_opc() \n
		This command generates the waveform files containing predistortion information within the amplifier application. All in
		all, the command generates three waveform files: AM/AM only, AM/PM only and AM/AM plus AM/PM. It also transfers these
		waveform files to the connected signal generator.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DPD:FILE:GENerate', opc_timeout_ms)

	def clone(self) -> 'Generate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
