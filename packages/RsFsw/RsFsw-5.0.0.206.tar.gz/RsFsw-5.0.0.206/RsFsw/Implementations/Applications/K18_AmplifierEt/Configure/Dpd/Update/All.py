from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:DPD:UPDate:ALL \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.update.all.set() \n
		This command updates the DPD shaping tables on the R&S SMW when new measurement data is available. In addition, this
		command also turns on the DPD (AM/AM and AM/PM) . Using one command only to do those things has the advantage of a
		slightly shorter execution time.
			INTRO_CMD_HELP: Alternatively, you can do that with: \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Update.set and
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amxm.State.set
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		"""
		self._core.io.write(f'CONFigure:DPD:UPDate:ALL')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DPD:UPDate:ALL \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.update.all.set_with_opc() \n
		This command updates the DPD shaping tables on the R&S SMW when new measurement data is available. In addition, this
		command also turns on the DPD (AM/AM and AM/PM) . Using one command only to do those things has the advantage of a
		slightly shorter execution time.
			INTRO_CMD_HELP: Alternatively, you can do that with: \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Update.set and
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amxm.State.set
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DPD:UPDate:ALL', opc_timeout_ms)
