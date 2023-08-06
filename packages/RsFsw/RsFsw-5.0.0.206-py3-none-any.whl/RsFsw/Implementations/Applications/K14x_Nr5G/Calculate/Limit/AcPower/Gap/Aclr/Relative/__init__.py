from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Types import DataType
from ..........Internal.StructBase import StructBase
from ..........Internal.ArgStruct import ArgStruct
from ..........Internal.ArgSingleList import ArgSingleList
from ..........Internal.ArgSingle import ArgSingle
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, lower_limit: float, upper_limit: float = None, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:ACLR[:RELative] \n
		Snippet: driver.applications.k14Xnr5G.calculate.limit.acPower.gap.aclr.relative.set(lower_limit = 1.0, upper_limit = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param lower_limit: No help available
			:param upper_limit: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('lower_limit', lower_limit, DataType.Float), ArgSingle('upper_limit', upper_limit, DataType.Float, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:ACLR:RELative {param}'.rstrip())

	# noinspection PyTypeChecker
	class RelativeStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower_Limit: float: No parameter help available
			- Upper_Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower_Limit'),
			ArgStruct.scalar_float('Upper_Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower_Limit: float = None
			self.Upper_Limit: float = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> RelativeStruct:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:ACLR[:RELative] \n
		Snippet: value: RelativeStruct = driver.applications.k14Xnr5G.calculate.limit.acPower.gap.aclr.relative.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: structure: for return value, see the help for RelativeStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:ACLR:RELative?', self.__class__.RelativeStruct())

	def clone(self) -> 'Relative':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Relative(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
