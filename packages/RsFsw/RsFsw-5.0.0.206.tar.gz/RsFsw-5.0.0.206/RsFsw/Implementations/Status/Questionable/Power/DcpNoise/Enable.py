from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, summary_bit: int, channel_name: str = None) -> None:
		"""SCPI: STATus:QUEStionable:POWer:DCPNoise:ENABle \n
		Snippet: driver.status.questionable.power.dcpNoise.enable.set(summary_bit = 1, channel_name = '1') \n
		No command help available \n
			:param summary_bit: No help available
			:param channel_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('summary_bit', summary_bit, DataType.Integer), ArgSingle('channel_name', channel_name, DataType.String, None, is_optional=True))
		self._core.io.write(f'STATus:QUEStionable:POWer:DCPNoise:ENABle {param}'.rstrip())

	# noinspection PyTypeChecker
	class EnableStruct(StructBase):
		"""Response structure. Fields: \n
			- Summary_Bit: int: No parameter help available
			- Channel_Name: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Summary_Bit'),
			ArgStruct.scalar_str('Channel_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Summary_Bit: int = None
			self.Channel_Name: str = None

	def get(self) -> EnableStruct:
		"""SCPI: STATus:QUEStionable:POWer:DCPNoise:ENABle \n
		Snippet: value: EnableStruct = driver.status.questionable.power.dcpNoise.enable.get() \n
		No command help available \n
			:return: structure: for return value, see the help for EnableStruct structure arguments."""
		return self._core.io.query_struct(f'STATus:QUEStionable:POWer:DCPNoise:ENABle?', self.__class__.EnableStruct())
