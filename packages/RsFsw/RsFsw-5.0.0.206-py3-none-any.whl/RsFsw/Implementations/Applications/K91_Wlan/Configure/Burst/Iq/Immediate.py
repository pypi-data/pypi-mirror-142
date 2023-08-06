from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:BURSt:IQ[:IMMediate] \n
		Snippet: driver.applications.k91Wlan.configure.burst.iq.immediate.set() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:BURSt:IQ:IMMediate', opc_timeout_ms)
