from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>[:CACLr]:RESult:ABSolute \n
		Snippet: value: str = driver.applications.k14Xnr5G.calculate.limit.acPower.gap.caclr.result.absolute.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		This command queries the absolute limit check results for the gap channels (MC ACLR measurements) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select absolute limit check mode evaluation mode ACLR: method RsFsw.Calculate.Limit.AcPower.Pmode.set. Combined measurements: [SENSe:]NR5G:ACPower:ALPMode \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: limit_check: Returns two values, one for the upper and one for the lower adjacent channel. PASSED Limit check has passed. FAILED Limit check has failed."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:CACLr:RESult:ABSolute?')
		return trim_str_response(response)
