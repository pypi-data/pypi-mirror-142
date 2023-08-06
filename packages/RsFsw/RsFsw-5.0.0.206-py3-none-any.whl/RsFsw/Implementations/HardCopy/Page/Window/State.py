from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: str, arg_1: str, arg_2: bool, window=repcap.Window.Default) -> None:
		"""SCPI: HCOPy:PAGE:WINDow<1|2>:STATe \n
		Snippet: driver.hardCopy.page.window.state.set(arg_0 = '1', arg_1 = '1', arg_2 = False, window = repcap.Window.Default) \n
		This command selects the windows to be included in the printout for method RsFsw.HardCopy.Content.set. \n
			:param arg_0: String containing the name of the channel. For a list of available channel types use method RsFsw.Instrument.ListPy.get_.
			:param arg_1: String containing the name of the existing window. By default, the name of a window is the same as its index. To determine the name and index of all active windows in the active channel, use the method RsFsw.Layout.Catalog.Window.get_ query.
			:param arg_2: 1 | 0 | ON | OFF 1 | ON The window is included in the printout. 0 | OFF The window is not included in the printout.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.String), ArgSingle('arg_1', arg_1, DataType.String), ArgSingle('arg_2', arg_2, DataType.Boolean))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'HCOPy:PAGE:WINDow{window_cmd_val}:STATe {param}'.rstrip())

	# noinspection PyTypeChecker
	class StateStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: str: String containing the name of the channel. For a list of available channel types use [CMDLINK: INSTrument:LIST? CMDLINK].
			- Arg_1: str: String containing the name of the existing window. By default, the name of a window is the same as its index. To determine the name and index of all active windows in the active channel, use the [CMDLINK: LAYout:CATalog[:WINDow]? CMDLINK] query.
			- Arg_2: bool: 1 | 0 | ON | OFF 1 | ON The window is included in the printout. 0 | OFF The window is not included in the printout."""
		__meta_args_list = [
			ArgStruct.scalar_str('Arg_0'),
			ArgStruct.scalar_str('Arg_1'),
			ArgStruct.scalar_bool('Arg_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: str = None
			self.Arg_1: str = None
			self.Arg_2: bool = None

	def get(self, window=repcap.Window.Default) -> StateStruct:
		"""SCPI: HCOPy:PAGE:WINDow<1|2>:STATe \n
		Snippet: value: StateStruct = driver.hardCopy.page.window.state.get(window = repcap.Window.Default) \n
		This command selects the windows to be included in the printout for method RsFsw.HardCopy.Content.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: structure: for return value, see the help for StateStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'HCOPy:PAGE:WINDow{window_cmd_val}:STATe?', self.__class__.StateStruct())
