from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:CONFigure:GENerator:INITialise[:IMMediate] \n
		Snippet: driver.applications.k30NoiseFigure.system.configure.generator.initialise.immediate.set() \n
		This command establishes a connection to the external generator. When you send the command, the application configures
		the generator once and turns on its RF output. Note that you have to establish a connection to the generator before you
		can perform the measurement. The command is available with option R&S FSW-B10. \n
		"""
		self._core.io.write(f'SYSTem:CONFigure:GENerator:INITialise:IMMediate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:CONFigure:GENerator:INITialise[:IMMediate] \n
		Snippet: driver.applications.k30NoiseFigure.system.configure.generator.initialise.immediate.set_with_opc() \n
		This command establishes a connection to the external generator. When you send the command, the application configures
		the generator once and turns on its RF output. Note that you have to establish a connection to the generator before you
		can perform the measurement. The command is available with option R&S FSW-B10. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:CONFigure:GENerator:INITialise:IMMediate', opc_timeout_ms)
