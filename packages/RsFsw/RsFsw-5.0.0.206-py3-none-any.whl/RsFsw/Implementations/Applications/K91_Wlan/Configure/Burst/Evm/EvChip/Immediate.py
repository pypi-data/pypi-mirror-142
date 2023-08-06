from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:BURSt:EVM:EVCHip[:IMMediate] \n
		Snippet: driver.applications.k91Wlan.configure.burst.evm.evChip.immediate.set() \n
		Both of these commands configure the measurement type to be EVM vs Chip for IEEE 802.11b and g (DSSS) standards.
		For compatibility reasons, the method RsFsw.Applications.K91_Wlan.Configure.Burst.Evm.Esymbol.Immediate.set command is
		also supported for the IEEE 802.11b and g (DSSS) standards. However, for new remote control programs use the LAYout
		commands (see 'Working with windows in the display') . Results are only displayed after a measurement is executed, e.g.
		using the method RsFsw.Applications.K10x_Lte.Initiate.Immediate.set command. Note that the CONF:BURS:<ResultType>:IMM
		commands change the screen layout to display the Magnitude Capture buffer in window 1 at the top of the screen and the
		selected result type in window 2 below that. Any other active windows are closed. Use the LAYout commands to change the
		display (see 'Working with windows in the display') . \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:BURSt:EVM:EVCHip:IMMediate', opc_timeout_ms)
