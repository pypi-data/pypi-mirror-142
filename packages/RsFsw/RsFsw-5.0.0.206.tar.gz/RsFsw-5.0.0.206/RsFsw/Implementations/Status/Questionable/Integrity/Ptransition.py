from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptransition:
	"""Ptransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptransition", core, parent)

	def set(self, bit_definition: int, channel_name: str = None) -> None:
		"""SCPI: STATus:QUEStionable:INTegrity:PTRansition \n
		Snippet: driver.status.questionable.integrity.ptransition.set(bit_definition = 1, channel_name = '1') \n
		No command help available \n
			:param bit_definition: No help available
			:param channel_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bit_definition', bit_definition, DataType.Integer), ArgSingle('channel_name', channel_name, DataType.String, None, is_optional=True))
		self._core.io.write(f'STATus:QUEStionable:INTegrity:PTRansition {param}'.rstrip())

	# noinspection PyTypeChecker
	class PtransitionStruct(StructBase):
		"""Response structure. Fields: \n
			- Bit_Definition: int: No parameter help available
			- Channel_Name: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Bit_Definition'),
			ArgStruct.scalar_str('Channel_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bit_Definition: int = None
			self.Channel_Name: str = None

	def get(self) -> PtransitionStruct:
		"""SCPI: STATus:QUEStionable:INTegrity:PTRansition \n
		Snippet: value: PtransitionStruct = driver.status.questionable.integrity.ptransition.get() \n
		No command help available \n
			:return: structure: for return value, see the help for PtransitionStruct structure arguments."""
		return self._core.io.query_struct(f'STATus:QUEStionable:INTegrity:PTRansition?', self.__class__.PtransitionStruct())
