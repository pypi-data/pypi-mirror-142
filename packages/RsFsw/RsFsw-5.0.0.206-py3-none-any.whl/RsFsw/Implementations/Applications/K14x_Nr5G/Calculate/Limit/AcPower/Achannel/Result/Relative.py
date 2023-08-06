from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

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

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> Results:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:ACHannel:RESult:RELative \n
		Snippet: value: Results = driver.applications.k14Xnr5G.calculate.limit.acPower.achannel.result.relative.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the relative limit check results for the adjacent channels (ACLR measurements) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select relative limit check mode ACLR: method RsFsw.Calculate.Limit.AcPower.Pmode.set. Combined measurements: [SENSe:]NR5G:ACPower:ALPMode \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: structure: for return value, see the help for Results structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:ACHannel:RESult:RELative?', self.__class__.Results())
