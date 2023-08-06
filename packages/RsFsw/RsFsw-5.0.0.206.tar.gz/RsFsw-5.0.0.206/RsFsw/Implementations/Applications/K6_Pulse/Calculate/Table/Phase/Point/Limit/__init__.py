from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, lower_limit: float, upper_limit: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TABLe:PHASe:POINt:LIMit \n
		Snippet: driver.applications.k6Pulse.calculate.table.phase.point.limit.set(lower_limit = 1.0, upper_limit = 1.0, window = repcap.Window.Default) \n
		Defines the valid value range for the limit check for the selected parameter if limit check is active
		(CALCulate<n>:TABLe:<ParameterGroup>:<Parameter>:LIMit:STATeON) . Commands for the parameter group <TSIDelobe> are only
		available if the additional option R&S FSW-K6S is installed. For details on the individual parameters see 'Pulse
		parameters'. \n
			:param lower_limit: Lower limit of the valid value range. Unit: S
			:param upper_limit: Upper limit of the valid value range. Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('lower_limit', lower_limit, DataType.Float), ArgSingle('upper_limit', upper_limit, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TABLe:PHASe:POINt:LIMit {param}'.rstrip())

	# noinspection PyTypeChecker
	class LimitStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower_Limit: float: Lower limit of the valid value range. Unit: S
			- Upper_Limit: float: Upper limit of the valid value range. Unit: S"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower_Limit'),
			ArgStruct.scalar_float('Upper_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower_Limit: float = None
			self.Upper_Limit: float = None

	def get(self, window=repcap.Window.Default) -> LimitStruct:
		"""SCPI: CALCulate<n>:TABLe:PHASe:POINt:LIMit \n
		Snippet: value: LimitStruct = driver.applications.k6Pulse.calculate.table.phase.point.limit.get(window = repcap.Window.Default) \n
		Defines the valid value range for the limit check for the selected parameter if limit check is active
		(CALCulate<n>:TABLe:<ParameterGroup>:<Parameter>:LIMit:STATeON) . Commands for the parameter group <TSIDelobe> are only
		available if the additional option R&S FSW-K6S is installed. For details on the individual parameters see 'Pulse
		parameters'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for LimitStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:TABLe:PHASe:POINt:LIMit?', self.__class__.LimitStruct())

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
