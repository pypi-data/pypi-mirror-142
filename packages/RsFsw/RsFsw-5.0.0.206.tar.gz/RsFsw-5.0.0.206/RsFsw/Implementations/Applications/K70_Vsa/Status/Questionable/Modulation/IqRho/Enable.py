from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, bit_definition: int, channel_name: str = None, window=repcap.Window.Default) -> None:
		"""SCPI: STATus:QUEStionable:MODulation<Window>:IQRHo:ENABle \n
		Snippet: driver.applications.k70Vsa.status.questionable.modulation.iqRho.enable.set(bit_definition = 1, channel_name = '1', window = repcap.Window.Default) \n
		This command controls the ENABle part of a register. The ENABle part allows true conditions in the EVENt part of the
		status register to be reported in the summary bit. If a bit is 1 in the enable register and its associated event bit
		transitions to true, a positive transition will occur in the summary bit reported to the next higher level. \n
			:param bit_definition: Range: 0 to 65535
			:param channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Modulation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bit_definition', bit_definition, DataType.Integer), ArgSingle('channel_name', channel_name, DataType.String, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'STATus:QUEStionable:MODulation{window_cmd_val}:IQRHo:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Response structure. Fields: \n
			- Bit_Definition: int: Range: 0 to 65535
			- Channel_Name: str: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		__meta_args_list = [
			ArgStruct.scalar_int('Bit_Definition'),
			ArgStruct.scalar_str('Channel_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bit_Definition: int = None
			self.Channel_Name: str = None

	def get(self, window=repcap.Window.Default) -> EnableStruct:
		"""SCPI: STATus:QUEStionable:MODulation<Window>:IQRHo:ENABle \n
		Snippet: value: EnableStruct = driver.applications.k70Vsa.status.questionable.modulation.iqRho.enable.get(window = repcap.Window.Default) \n
		This command controls the ENABle part of a register. The ENABle part allows true conditions in the EVENt part of the
		status register to be reported in the summary bit. If a bit is 1 in the enable register and its associated event bit
		transitions to true, a positive transition will occur in the summary bit reported to the next higher level. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Modulation')
			:return: structure: for return value, see the help for EnableStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'STATus:QUEStionable:MODulation{window_cmd_val}:IQRHo:ENABle?', self.__class__.EnableStruct())
