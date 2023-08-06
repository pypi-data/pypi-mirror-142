from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:DPD:FILE:GENerate:ALL \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.file.generate.all.set() \n
		This command generates the waveform files containing predistortion information within the amplifier application. All in
		all, the command generates three waveform files: AM/AM only, AM/PM only and AM/AM plus AM/PM. It also transfers these
		waveform files to the connected signal generator and turns on the AM/AM and AM/PM DPDs.
			INTRO_CMD_HELP: Alternatively, you can do that with: \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.File.Generate.set and
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amxm.State.set
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:DPD:FILE:GENerate:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DPD:FILE:GENerate:ALL \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.file.generate.all.set_with_opc() \n
		This command generates the waveform files containing predistortion information within the amplifier application. All in
		all, the command generates three waveform files: AM/AM only, AM/PM only and AM/AM plus AM/PM. It also transfers these
		waveform files to the connected signal generator and turns on the AM/AM and AM/PM DPDs.
			INTRO_CMD_HELP: Alternatively, you can do that with: \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.File.Generate.set and
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amxm.State.set
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DPD:FILE:GENerate:ALL', opc_timeout_ms)
