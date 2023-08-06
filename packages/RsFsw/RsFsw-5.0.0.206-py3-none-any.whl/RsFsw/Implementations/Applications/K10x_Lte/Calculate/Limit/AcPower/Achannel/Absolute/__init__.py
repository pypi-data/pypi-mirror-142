from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


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

	def set(self, lower_limit: float, upper_limit: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel:ABSolute \n
		Snippet: driver.applications.k10Xlte.calculate.limit.acPower.achannel.absolute.set(lower_limit = 1.0, upper_limit = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param lower_limit: No help available
			:param upper_limit: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('lower_limit', lower_limit, DataType.Float), ArgSingle('upper_limit', upper_limit, DataType.Float))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:ABSolute {param}'.rstrip())

	# noinspection PyTypeChecker
	class Limits(StructBase):
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

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> Limits:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel:ABSolute \n
		Snippet: value: Limits = driver.applications.k10Xlte.calculate.limit.acPower.achannel.absolute.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for Limits structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:ABSolute?', self.__class__.Limits())

	def clone(self) -> 'Absolute':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Absolute(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
