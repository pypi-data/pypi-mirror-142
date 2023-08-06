from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nr5G:
	"""Nr5G commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nr5G", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:GENerator:SETTings:UPDate:NR5G \n
		Snippet: driver.applications.k14Xnr5G.configure.generator.settings.update.nr5G.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:GENerator:SETTings:UPDate:NR5G')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:GENerator:SETTings:UPDate:NR5G \n
		Snippet: driver.applications.k14Xnr5G.configure.generator.settings.update.nr5G.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:GENerator:SETTings:UPDate:NR5G', opc_timeout_ms)
