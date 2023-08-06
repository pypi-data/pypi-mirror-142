from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Update:
	"""Update commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("update", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:SETTings:NOTCh:UPDate \n
		Snippet: driver.configure.generator.npratio.settings.notch.update.set() \n
		Applies all notch settings to the connected signal generator once. \n
		"""
		self._core.io.write(f'CONFigure:GENerator:NPRatio:SETTings:NOTCh:UPDate')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:SETTings:NOTCh:UPDate \n
		Snippet: driver.configure.generator.npratio.settings.notch.update.set_with_opc() \n
		Applies all notch settings to the connected signal generator once. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:GENerator:NPRatio:SETTings:NOTCh:UPDate', opc_timeout_ms)
