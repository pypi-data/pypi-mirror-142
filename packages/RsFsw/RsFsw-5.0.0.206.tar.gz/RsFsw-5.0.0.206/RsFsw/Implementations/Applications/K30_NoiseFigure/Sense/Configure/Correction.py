from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correction:
	"""Correction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:CONFigure:CORRection \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.correction.set() \n
		This command configures the software to perform calibration measurements. Using method RsFsw.Applications.K10x_Lte.
		Initiate.Immediate.set then initiates a calibration instead of the actual measurement, until you deliberately select one
		of the normal measurements again with one of the following commands.
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- [SENSe:]CONFigure:FREQuency:CONTinuous
			- [SENSe:]CONFigure:FREQuency:SINGle
			- [SENSe:]CONFigure:LIST:CONTinuous
			- [SENSe:]CONFigure:LIST:SINGle
		Note that calibration data is used only when the second stage correction mode has been turned on with
		[SENSe:]CORRection[:STATe]. \n
		"""
		self._core.io.write(f'SENSe:CONFigure:CORRection')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CONFigure:CORRection \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.correction.set_with_opc() \n
		This command configures the software to perform calibration measurements. Using method RsFsw.Applications.K10x_Lte.
		Initiate.Immediate.set then initiates a calibration instead of the actual measurement, until you deliberately select one
		of the normal measurements again with one of the following commands.
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- [SENSe:]CONFigure:FREQuency:CONTinuous
			- [SENSe:]CONFigure:FREQuency:SINGle
			- [SENSe:]CONFigure:LIST:CONTinuous
			- [SENSe:]CONFigure:LIST:SINGle
		Note that calibration data is used only when the second stage correction mode has been turned on with
		[SENSe:]CORRection[:STATe]. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CONFigure:CORRection', opc_timeout_ms)
