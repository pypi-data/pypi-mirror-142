from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Next:
	"""Next commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("next", core, parent)

	def set(self) -> None:
		"""SCPI: MMEMory:STORe:STATe:NEXT \n
		Snippet: driver.massMemory.store.state.next.set() \n
		This command saves the current instrument configuration in a *.dfl file. The file name depends on the one you have set
		with method RsFsw.MassMemory.Store.State.set. This command adds a consecutive number to the file name. Secure User Mode
		In secure user mode, settings that are stored on the instrument are stored to volatile memory, which is restricted to 256
		MB. Thus, a 'memory limit reached' error can occur although the hard disk indicates that storage space is still available.
		To store data permanently, select an external storage location such as a USB memory device. For details, see 'Protecting
		data using the secure user mode'. \n
		"""
		self._core.io.write(f'MMEMory:STORe:STATe:NEXT')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: MMEMory:STORe:STATe:NEXT \n
		Snippet: driver.massMemory.store.state.next.set_with_opc() \n
		This command saves the current instrument configuration in a *.dfl file. The file name depends on the one you have set
		with method RsFsw.MassMemory.Store.State.set. This command adds a consecutive number to the file name. Secure User Mode
		In secure user mode, settings that are stored on the instrument are stored to volatile memory, which is restricted to 256
		MB. Thus, a 'memory limit reached' error can occur although the hard disk indicates that storage space is still available.
		To store data permanently, select an external storage location such as a USB memory device. For details, see 'Protecting
		data using the secure user mode'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'MMEMory:STORe:STATe:NEXT', opc_timeout_ms)
