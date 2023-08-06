from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
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
			- Lower_Ach: enums.CheckResult: No parameter help available
			- Upper_Ach: enums.CheckResult: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Lower_Ach', enums.CheckResult),
			ArgStruct.scalar_enum('Upper_Ach', enums.CheckResult)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Lower_Ach: enums.CheckResult = None
			self.Upper_Ach: enums.CheckResult = None

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> GetStruct:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel:RESult \n
		Snippet: value: GetStruct = driver.applications.k91Wlan.calculate.limit.acPower.achannel.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the state of the limit check for the adjacent or alternate channels in an ACLR measurement. To get a
		valid result, you have to perform a complete measurement with synchronization to the end of the measurement before
		reading out the result. This is only possible for single measurement mode. See also method RsFsw.Applications.K10x_Lte.
		Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:RESult?', self.__class__.GetStruct())
