from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Continuous:
	"""Continuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("continuous", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:CONFigure:FREQuency:CONTinuous \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.frequency.continuous.set() \n
		This command configures the software to perform a single frequency measurement in continuous sweep mode. \n
		"""
		self._core.io.write(f'SENSe:CONFigure:FREQuency:CONTinuous')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:CONFigure:FREQuency:CONTinuous \n
		Snippet: driver.applications.k30NoiseFigure.sense.configure.frequency.continuous.set_with_opc() \n
		This command configures the software to perform a single frequency measurement in continuous sweep mode. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:CONFigure:FREQuency:CONTinuous', opc_timeout_ms)
