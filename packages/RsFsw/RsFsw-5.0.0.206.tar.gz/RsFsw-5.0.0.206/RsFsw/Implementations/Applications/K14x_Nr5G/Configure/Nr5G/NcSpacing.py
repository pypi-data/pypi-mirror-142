from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NcSpacing:
	"""NcSpacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ncSpacing", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure[:NR5G]:NCSPacing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.ncSpacing.set() \n
		This command resets the channel spacing of component carriers to its default value. \n
		"""
		self._core.io.write(f'CONFigure:NR5G:NCSPacing')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure[:NR5G]:NCSPacing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.ncSpacing.set_with_opc() \n
		This command resets the channel spacing of component carriers to its default value. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:NCSPacing', opc_timeout_ms)
