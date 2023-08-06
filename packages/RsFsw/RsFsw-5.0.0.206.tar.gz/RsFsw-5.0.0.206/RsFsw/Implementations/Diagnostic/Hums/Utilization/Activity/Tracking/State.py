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

	def set(self, idn: float, state: bool) -> None:
		"""SCPI: DIAGnostic:HUMS:UTILization:ACTivity:TRACking:STATe \n
		Snippet: driver.diagnostic.hums.utilization.activity.tracking.state.set(idn = 1.0, state = False) \n
		No command help available \n
			:param idn: No help available
			:param state: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('idn', idn, DataType.Float), ArgSingle('state', state, DataType.Boolean))
		self._core.io.write(f'DIAGnostic:HUMS:UTILization:ACTivity:TRACking:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Idn: float: No parameter help available
			- State: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Idn'),
			ArgStruct.scalar_bool('State')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: float = None
			self.State: bool = None

	def get(self) -> StateStruct:
		"""SCPI: DIAGnostic:HUMS:UTILization:ACTivity:TRACking:STATe \n
		Snippet: value: StateStruct = driver.diagnostic.hums.utilization.activity.tracking.state.get() \n
		No command help available \n
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:HUMS:UTILization:ACTivity:TRACking:STATe?', self.__class__.StateStruct())
