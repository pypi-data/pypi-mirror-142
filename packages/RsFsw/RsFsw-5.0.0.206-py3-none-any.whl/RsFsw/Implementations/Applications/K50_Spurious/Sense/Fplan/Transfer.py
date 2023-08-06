from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transfer:
	"""Transfer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transfer", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:FPLan:TRANsfer \n
		Snippet: driver.applications.k50Spurious.sense.fplan.transfer.set() \n
		This command will transfer all frequencies that result out of the current frequency plan settings to the directed search
		settings. For details see 'Frequency plan and spur identification'. \n
		"""
		self._core.io.write(f'SENSe:FPLan:TRANsfer')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:FPLan:TRANsfer \n
		Snippet: driver.applications.k50Spurious.sense.fplan.transfer.set_with_opc() \n
		This command will transfer all frequencies that result out of the current frequency plan settings to the directed search
		settings. For details see 'Frequency plan and spur identification'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:FPLan:TRANsfer', opc_timeout_ms)
