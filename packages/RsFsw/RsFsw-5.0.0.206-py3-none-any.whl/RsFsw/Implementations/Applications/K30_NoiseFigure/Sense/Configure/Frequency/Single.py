from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Single:
	"""Single commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("single", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:CONFigure:FREQuency:SINGle \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.frequency.single.set() \n
		This command configures the software to perform a single frequency measurement in single sweep mode. \n
		"""
		self._core.io.write(f'SENSe:CONFigure:FREQuency:SINGle')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CONFigure:FREQuency:SINGle \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.frequency.single.set_with_opc() \n
		This command configures the software to perform a single frequency measurement in single sweep mode. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CONFigure:FREQuency:SINGle', opc_timeout_ms)
