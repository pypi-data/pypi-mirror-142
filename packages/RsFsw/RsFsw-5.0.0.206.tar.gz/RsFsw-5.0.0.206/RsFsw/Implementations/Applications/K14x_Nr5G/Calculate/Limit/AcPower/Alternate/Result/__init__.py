from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import Absolute
			self._absolute = Absolute(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import Relative
			self._relative = Relative(self._core, self._cmd_group)
		return self._relative

	# noinspection PyTypeChecker
	class Results(StructBase):
		"""Response structure. Fields: \n
			- Upper_Limit: enums.CheckResult: No parameter help available
			- Lower_Limit: enums.CheckResult: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Upper_Limit', enums.CheckResult),
			ArgStruct.scalar_enum('Lower_Limit', enums.CheckResult)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Upper_Limit: enums.CheckResult = None
			self.Lower_Limit: enums.CheckResult = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, channel=repcap.Channel.Default) -> Results:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ALTernate<ch>:RESult \n
		Snippet: value: Results = driver.applications.k14Xnr5G.calculate.limit.acPower.alternate.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, channel = repcap.Channel.Default) \n
		This command queries the limit check results for the alternate channels during ACLR measurements. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
			:return: structure: for return value, see the help for Results structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ALTernate{channel_cmd_val}:RESult?', self.__class__.Results())

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
