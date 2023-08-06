from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, limit: float, reserved: float = None, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>[:AUTO]:ABSolute \n
		Snippet: driver.calculate.limit.acPower.gap.auto.absolute.set(limit = 1.0, reserved = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		This command defines the absolute limit of the specified gap (CACLR) channel. If you define both an absolute limit and a
		relative limit, the R&S FSW uses the lower value for the limit check. \n
			:param limit: Defines the absolute limit of the specified gap channel. Unit: dBm
			:param reserved: Ignored.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('limit', limit, DataType.Float), ArgSingle('reserved', reserved, DataType.Float, None, is_optional=True))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:AUTO:ABSolute {param}'.rstrip())

	# noinspection PyTypeChecker
	class AbsoluteStruct(StructBase):
		"""Response structure. Fields: \n
			- Limit: float: Defines the absolute limit of the specified gap channel. Unit: dBm
			- Reserved: float: Ignored."""
		__meta_args_list = [
			ArgStruct.scalar_float('Limit'),
			ArgStruct.scalar_float('Reserved')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Limit: float = None
			self.Reserved: float = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> AbsoluteStruct:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>[:AUTO]:ABSolute \n
		Snippet: value: AbsoluteStruct = driver.calculate.limit.acPower.gap.auto.absolute.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		This command defines the absolute limit of the specified gap (CACLR) channel. If you define both an absolute limit and a
		relative limit, the R&S FSW uses the lower value for the limit check. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: structure: for return value, see the help for AbsoluteStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:AUTO:ABSolute?', self.__class__.AbsoluteStruct())

	def clone(self) -> 'Absolute':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Absolute(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
