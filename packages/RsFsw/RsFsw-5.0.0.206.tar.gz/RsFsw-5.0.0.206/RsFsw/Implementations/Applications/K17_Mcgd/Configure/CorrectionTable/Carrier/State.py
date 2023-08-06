from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, index: int, carrier_state: bool) -> None:
		"""SCPI: CONFigure:CTABle:CARRier:STATe \n
		Snippet: driver.applications.k17Mcgd.configure.correctionTable.carrier.state.set(index = 1, carrier_state = False) \n
		Sets the state of a specific carrier of the carrier table. \n
			:param index: Carrier position
			:param carrier_state: ON | OFF
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('carrier_state', carrier_state, DataType.Boolean))
		self._core.io.write(f'CONFigure:CTABle:CARRier:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: int: Carrier position
			- Carrier_State: bool: ON | OFF"""
		__meta_args_list = [
			ArgStruct.scalar_int('Index'),
			ArgStruct.scalar_bool('Carrier_State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: int = None
			self.Carrier_State: bool = None

	def get(self) -> StateStruct:
		"""SCPI: CONFigure:CTABle:CARRier:STATe \n
		Snippet: value: StateStruct = driver.applications.k17Mcgd.configure.correctionTable.carrier.state.get() \n
		Sets the state of a specific carrier of the carrier table. \n
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:CTABle:CARRier:STATe?', self.__class__.StateStruct())
