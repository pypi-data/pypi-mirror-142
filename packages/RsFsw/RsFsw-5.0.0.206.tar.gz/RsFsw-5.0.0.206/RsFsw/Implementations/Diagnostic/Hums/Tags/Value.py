from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, idn: float, key: str, value: str) -> None:
		"""SCPI: DIAGnostic:HUMS:TAGS:VALue \n
		Snippet: driver.diagnostic.hums.tags.value.set(idn = 1.0, key = '1', value = '1') \n
		This command adds or modifies a key-value pair (device tag) . The query returns the key-value pair for a given ID or an
		empty string if the ID is unknown. \n
			:param idn: 0 - 31 ID number of the tag you want to modify or query. To identify the ID number, query all device tags from the system first. For more information, read here method RsFsw.Diagnostic.Hums.Tags.All.get_.
			:param key: String containing key name of the queried tag.
			:param value: String containing value of the queried tag.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('idn', idn, DataType.Float), ArgSingle('key', key, DataType.String), ArgSingle('value', value, DataType.String))
		self._core.io.write(f'DIAGnostic:HUMS:TAGS:VALue {param}'.rstrip())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Response structure. Fields: \n
			- Idn: float: 0 - 31 ID number of the tag you want to modify or query. To identify the ID number, query all device tags from the system first. For more information, read here [CMDLINK: DIAGnostic:HUMS:TAGS:ALL? CMDLINK].
			- Key: str: String containing key name of the queried tag.
			- Value: str: String containing value of the queried tag."""
		__meta_args_list = [
			ArgStruct.scalar_float('Idn'),
			ArgStruct.scalar_str('Key'),
			ArgStruct.scalar_str('Value')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: float = None
			self.Key: str = None
			self.Value: str = None

	def get(self) -> ValueStruct:
		"""SCPI: DIAGnostic:HUMS:TAGS:VALue \n
		Snippet: value: ValueStruct = driver.diagnostic.hums.tags.value.get() \n
		This command adds or modifies a key-value pair (device tag) . The query returns the key-value pair for a given ID or an
		empty string if the ID is unknown. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:HUMS:TAGS:VALue?', self.__class__.ValueStruct())
