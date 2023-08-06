from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:EXECute \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.execute.set() \n
		Transfers configuration assistant settings to the carrier table. \n
		"""
		self._core.io.write(f'CONFigure:CTABle:EDIT:CARRier:EXECute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:CTABle:EDIT:CARRier:EXECute \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.edit.carrier.execute.set_with_opc() \n
		Transfers configuration assistant settings to the carrier table. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:CTABle:EDIT:CARRier:EXECute', opc_timeout_ms)
