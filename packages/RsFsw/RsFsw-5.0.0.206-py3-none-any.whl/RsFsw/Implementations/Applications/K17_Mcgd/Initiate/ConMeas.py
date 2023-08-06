from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConMeas:
	"""ConMeas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conMeas", core, parent)

	def set(self) -> None:
		"""SCPI: INITiate:CONMeas \n
		Snippet: driver.applications.k17Mcgd.initiate.conMeas.set() \n
		This command restarts a (single) measurement that has been stopped (using method RsFsw.#Abort CMDLINKRESOLVED]) or
		finished in single sweep mode. The measurement is restarted at the beginning, not where the previous measurement was
		stopped. As opposed to [CMDLINKRESOLVED Applications.K10x_Lte.Initiate.Immediate.set, this command does not reset traces
		in maxhold, minhold or average mode. Therefore it can be used to continue measurements using maxhold or averaging
		functions. \n
		"""
		self._core.io.write(f'INITiate:CONMeas')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: INITiate:CONMeas \n
		Snippet: driver.applications.k17Mcgd.initiate.conMeas.set_with_opc() \n
		This command restarts a (single) measurement that has been stopped (using method RsFsw.#Abort CMDLINKRESOLVED]) or
		finished in single sweep mode. The measurement is restarted at the beginning, not where the previous measurement was
		stopped. As opposed to [CMDLINKRESOLVED Applications.K10x_Lte.Initiate.Immediate.set, this command does not reset traces
		in maxhold, minhold or average mode. Therefore it can be used to continue measurements using maxhold or averaging
		functions. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'INITiate:CONMeas', opc_timeout_ms)
