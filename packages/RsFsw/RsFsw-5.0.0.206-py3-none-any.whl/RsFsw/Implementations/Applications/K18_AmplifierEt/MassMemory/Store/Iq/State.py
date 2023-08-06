from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, number: int, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe \n
		Snippet: driver.applications.k18AmplifierEt.massMemory.store.iq.state.set(number = 1, filename = '1', store = repcap.Store.Default) \n
		This command stores the currently captured I/Q data to a file. In secure user mode, settings that are stored on the
		instrument are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory limit reached' error can occur
		although the hard disk indicates that storage space is still available. To store data permanently, select an external
		storage location such as a USB memory device. For details, see 'Protecting Data Using the Secure User Mode'. \n
			:param number: Always '1'.
			:param filename: String containing the path and file name. The file type is .iq.tar.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number', number, DataType.Integer), ArgSingle('filename', filename, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:STATe {param}'.rstrip())
