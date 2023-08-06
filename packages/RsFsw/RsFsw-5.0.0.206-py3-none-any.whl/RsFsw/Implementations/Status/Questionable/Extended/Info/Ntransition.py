from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ntransition:
	"""Ntransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntransition", core, parent)

	def set(self, summary_bit: int, channel_name: str = None) -> None:
		"""SCPI: STATus:QUEStionable:EXTended:INFO:NTRansition \n
		Snippet: driver.status.questionable.extended.info.ntransition.set(summary_bit = 1, channel_name = '1') \n
		These commands control the Negative TRansition part of a register. Setting a bit causes a 1 to 0 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:param summary_bit: No help available
			:param channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('summary_bit', summary_bit, DataType.Integer), ArgSingle('channel_name', channel_name, DataType.String, None, is_optional=True))
		self._core.io.write(f'STATus:QUEStionable:EXTended:INFO:NTRansition {param}'.rstrip())

	# noinspection PyTypeChecker
	class NtransitionStruct(StructBase):
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

	def get(self) -> NtransitionStruct:
		"""SCPI: STATus:QUEStionable:EXTended:INFO:NTRansition \n
		Snippet: value: NtransitionStruct = driver.status.questionable.extended.info.ntransition.get() \n
		These commands control the Negative TRansition part of a register. Setting a bit causes a 1 to 0 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:return: structure: for return value, see the help for NtransitionStruct structure arguments."""
		return self._core.io.query_struct(f'STATus:QUEStionable:EXTended:INFO:NTRansition?', self.__class__.NtransitionStruct())
