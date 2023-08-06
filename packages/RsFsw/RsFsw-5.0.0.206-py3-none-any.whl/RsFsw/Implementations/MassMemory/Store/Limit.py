from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def set(self, filename: str, limit_line_name: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:LIMit \n
		Snippet: driver.massMemory.store.limit.set(filename = '1', limit_line_name = '1', store = repcap.Store.Default) \n
		This command exports limit line data to an ASCII (CSV) file. For details on the file format see 'Reference: limit line
		file format'. \n
			:param filename: String containing the path and name of the target file.
			:param limit_line_name: Name of the limit line to be exported.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filename', filename, DataType.String), ArgSingle('limit_line_name', limit_line_name, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:LIMit {param}'.rstrip())

	# noinspection PyTypeChecker
	class LimitStruct(StructBase):
		"""Response structure. Fields: \n
			- Filename: str: String containing the path and name of the target file.
			- Limit_Line_Name: str: Name of the limit line to be exported."""
		__meta_args_list = [
			ArgStruct.scalar_str('Filename'),
			ArgStruct.scalar_str('Limit_Line_Name')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Filename: str = None
			self.Limit_Line_Name: str = None

	def get(self, store=repcap.Store.Default) -> LimitStruct:
		"""SCPI: MMEMory:STORe<n>:LIMit \n
		Snippet: value: LimitStruct = driver.massMemory.store.limit.get(store = repcap.Store.Default) \n
		This command exports limit line data to an ASCII (CSV) file. For details on the file format see 'Reference: limit line
		file format'. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: structure: for return value, see the help for LimitStruct structure arguments."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		return self._core.io.query_struct(f'MMEMory:STORe{store_cmd_val}:LIMit?', self.__class__.LimitStruct())
