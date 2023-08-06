from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Settings:
	"""Settings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("settings", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:SETTings \n
		Snippet: driver.applications.k18AmplifierEt.configure.settings.set() \n
		This command transfers the current generator configuration into the amplifier application. Make sure to synchronize with
		*OPC? or *WAI to make sure that the command was successfully applied on the generator before sending the next command. \n
		"""
		self._core.io.write(f'CONFigure:SETTings')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:SETTings \n
		Snippet: driver.applications.k18AmplifierEt.configure.settings.set_with_opc() \n
		This command transfers the current generator configuration into the amplifier application. Make sure to synchronize with
		*OPC? or *WAI to make sure that the command was successfully applied on the generator before sending the next command. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:SETTings', opc_timeout_ms)
