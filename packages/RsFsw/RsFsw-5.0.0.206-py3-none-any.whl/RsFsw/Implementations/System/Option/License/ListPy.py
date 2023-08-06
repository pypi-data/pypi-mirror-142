from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Option: str: string value Name of an option whose license is set.
			- State: enums.OptionState: ON | OFF | OCCupy State of the license ON Floating license enabled OFF Floating license disabled OCCupy Occupied license
			- Days: float: The time period an occupied license is stored locally after it is retrieved from the license server. Range: 1 to 7, Unit: days"""
		__meta_args_list = [
			ArgStruct.scalar_str('Option'),
			ArgStruct.scalar_enum('State', enums.OptionState),
			ArgStruct.scalar_float('Days')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Option: str = None
			self.State: enums.OptionState = None
			self.Days: float = None

	def get(self) -> GetStruct:
		"""SCPI: SYSTem:OPTion:LICense[:LIST] \n
		Snippet: value: GetStruct = driver.system.option.license.listPy.get() \n
		Defines the availability of floating licenses for the R&S FSW. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'SYSTem:OPTion:LICense:LIST?', self.__class__.GetStruct())
