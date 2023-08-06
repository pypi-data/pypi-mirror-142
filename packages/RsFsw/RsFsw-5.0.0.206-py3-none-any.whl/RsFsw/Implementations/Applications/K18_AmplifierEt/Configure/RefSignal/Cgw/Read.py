from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:REFSignal:CGW:READ \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cgw.read.set() \n
		This command transfers a reference signal designed on a signal generator into the R&S FSW-K18. \n
		"""
		self._core.io.write(f'CONFigure:REFSignal:CGW:READ')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:REFSignal:CGW:READ \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cgw.read.set_with_opc() \n
		This command transfers a reference signal designed on a signal generator into the R&S FSW-K18. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:REFSignal:CGW:READ', opc_timeout_ms)
