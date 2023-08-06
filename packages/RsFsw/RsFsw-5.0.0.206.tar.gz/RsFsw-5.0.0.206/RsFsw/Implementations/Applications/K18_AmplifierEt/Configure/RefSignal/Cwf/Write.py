from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Write:
	"""Write commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("write", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:REFSignal:CWF:WRITe \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cwf.write.set() \n
		This command loads a reference signal based on a waveform file into the application. When you turn on the reference
		signal export to the generator (method RsFsw.Applications.K18_AmplifierEt.Configure.RefSignal.Cwf.EtGenerator.State.set) ,
		the command also transfers the waveform file to the generator. Make sure to synchronize with *OPC? or *WAI to make sure
		that the command was successfully applied on the generator before sending the next command. \n
		"""
		self._core.io.write(f'CONFigure:REFSignal:CWF:WRITe')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:REFSignal:CWF:WRITe \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cwf.write.set_with_opc() \n
		This command loads a reference signal based on a waveform file into the application. When you turn on the reference
		signal export to the generator (method RsFsw.Applications.K18_AmplifierEt.Configure.RefSignal.Cwf.EtGenerator.State.set) ,
		the command also transfers the waveform file to the generator. Make sure to synchronize with *OPC? or *WAI to make sure
		that the command was successfully applied on the generator before sending the next command. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:REFSignal:CWF:WRITe', opc_timeout_ms)
