from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Write:
	"""Write commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("write", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:WRITe \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.write.set() \n
		This command internally generates the reference signal based on the signal characteristics that you have defined.
		The waveform file that has been created is loaded into the DSP of the R&S FSW-K18 and is additionally transferred into
		the ARB of the signal generator. Make sure to synchronize with *OPC? or *WAI to make sure that the command was
		successfully applied on the generator before sending the next command. \n
		"""
		self._core.io.write(f'CONFigure:REFSignal:GOS:WRITe')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:WRITe \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.write.set_with_opc() \n
		This command internally generates the reference signal based on the signal characteristics that you have defined.
		The waveform file that has been created is loaded into the DSP of the R&S FSW-K18 and is additionally transferred into
		the ARB of the signal generator. Make sure to synchronize with *OPC? or *WAI to make sure that the command was
		successfully applied on the generator before sending the next command. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:REFSignal:GOS:WRITe', opc_timeout_ms)
