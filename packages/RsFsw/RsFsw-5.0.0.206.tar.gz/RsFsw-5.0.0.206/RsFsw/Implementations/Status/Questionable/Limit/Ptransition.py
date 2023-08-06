from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptransition:
	"""Ptransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptransition", core, parent)

	def set(self, summary_bit: int, channel_name: str = None, window=repcap.Window.Default) -> None:
		"""SCPI: STATus:QUEStionable:LIMit<1|2|3|4>:PTRansition \n
		Snippet: driver.status.questionable.limit.ptransition.set(summary_bit = 1, channel_name = '1', window = repcap.Window.Default) \n
		These commands control the Positive TRansition part of a register. Setting a bit causes a 0 to 1 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:param summary_bit: No help available
			:param channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('summary_bit', summary_bit, DataType.Integer), ArgSingle('channel_name', channel_name, DataType.String, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'STATus:QUEStionable:LIMit{window_cmd_val}:PTRansition {param}'.rstrip())

	# noinspection PyTypeChecker
	class PtransitionStruct(StructBase):
		"""Response structure. Fields: \n
			- Summary_Bit: int: No parameter help available
			- Channel_Name: str: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		__meta_args_list = [
			ArgStruct.scalar_int('Summary_Bit'),
			ArgStruct.scalar_str('Channel_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Summary_Bit: int = None
			self.Channel_Name: str = None

	def get(self, window=repcap.Window.Default) -> PtransitionStruct:
		"""SCPI: STATus:QUEStionable:LIMit<1|2|3|4>:PTRansition \n
		Snippet: value: PtransitionStruct = driver.status.questionable.limit.ptransition.get(window = repcap.Window.Default) \n
		These commands control the Positive TRansition part of a register. Setting a bit causes a 0 to 1 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for PtransitionStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'STATus:QUEStionable:LIMit{window_cmd_val}:PTRansition?', self.__class__.PtransitionStruct())
