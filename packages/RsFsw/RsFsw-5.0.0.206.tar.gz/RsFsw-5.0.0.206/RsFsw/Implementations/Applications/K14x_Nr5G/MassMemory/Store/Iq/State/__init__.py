from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def set(self, arg_0: int, arg_1: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe \n
		Snippet: driver.applications.k14Xnr5G.massMemory.store.iq.state.set(arg_0 = 1, arg_1 = '1', store = repcap.Store.Default) \n
		This command saves I/Q data to a file. \n
			:param arg_0: No help available
			:param arg_1: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Integer), ArgSingle('arg_1', arg_1, DataType.String))
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: int: No parameter help available
			- Arg_1: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Arg_0'),
			ArgStruct.scalar_str('Arg_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: int = None
			self.Arg_1: str = None

	def get(self, store=repcap.Store.Default) -> StateStruct:
		"""SCPI: MMEMory:STORe<n>:IQ:STATe \n
		Snippet: value: StateStruct = driver.applications.k14Xnr5G.massMemory.store.iq.state.get(store = repcap.Store.Default) \n
		This command saves I/Q data to a file. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		return self._core.io.query_struct(f'MMEMory:STORe{store_cmd_val}:IQ:STATe?', self.__class__.StateStruct())

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
