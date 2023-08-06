from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Next:
	"""Next commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("next", core, parent)

	def set(self) -> None:
		"""SCPI: HCOPy[:IMMediate]:NEXT \n
		Snippet: driver.hardCopy.immediate.next.set() \n
		This command initiates a print job. If you are printing to a file, the file name depends on method RsFsw.MassMemory.Name.
		set. This command adds a consecutive number to the file name. \n
		"""
		self._core.io.write(f'HCOPy:IMMediate:NEXT')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: HCOPy[:IMMediate]:NEXT \n
		Snippet: driver.hardCopy.immediate.next.set_with_opc() \n
		This command initiates a print job. If you are printing to a file, the file name depends on method RsFsw.MassMemory.Name.
		set. This command adds a consecutive number to the file name. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:IMMediate:NEXT', opc_timeout_ms)
