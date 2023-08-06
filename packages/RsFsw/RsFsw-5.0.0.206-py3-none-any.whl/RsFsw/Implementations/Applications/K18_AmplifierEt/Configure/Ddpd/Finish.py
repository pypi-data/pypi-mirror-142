from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Finish:
	"""Finish commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("finish", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:DDPD:FINish \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.finish.set() \n
		This command stops a DPD sequence before all iterations are done and keeps the predistorted I/Q data that have been
		calculated.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Initiate a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
		"""
		self._core.io.write(f'CONFigure:DDPD:FINish')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:DDPD:FINish \n
		Snippet: driver.applications.k18AmplifierEt.configure.ddpd.finish.set_with_opc() \n
		This command stops a DPD sequence before all iterations are done and keeps the predistorted I/Q data that have been
		calculated.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Initiate a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:DDPD:FINish', opc_timeout_ms)
