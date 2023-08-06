from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Lower_Chan: float: text value The state of the limit check for the lower alternate or adjacent channels. PASSED Limit check has passed. FAIL Limit check has failed.
			- Upper_Chan: float: text value The state of the limit check for the upper alternate or adjacent channels. PASSED Limit check has passed. FAIL Limit check has failed."""
		__meta_args_list = [
			ArgStruct.scalar_float('Lower_Chan'),
			ArgStruct.scalar_float('Upper_Chan')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower_Chan: float = None
			self.Upper_Chan: float = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, channel=repcap.Channel.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ALTernate<ch>:RESult \n
		Snippet: value: GetStruct = driver.applications.k91Wlan.calculate.limit.acPower.alternate.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, channel = repcap.Channel.Default) \n
		This command queries the state of the limit check for the adjacent or alternate channels in an ACLR measurement. To get a
		valid result, you have to perform a complete measurement with synchronization to the end of the measurement before
		reading out the result. This is only possible for single measurement mode. See also method RsFsw.Applications.K10x_Lte.
		Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ALTernate{channel_cmd_val}:RESult?', self.__class__.GetStruct())
