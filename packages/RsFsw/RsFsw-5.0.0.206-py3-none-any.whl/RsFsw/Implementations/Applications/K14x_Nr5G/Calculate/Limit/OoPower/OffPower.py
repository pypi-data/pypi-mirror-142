from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffPower:
	"""OffPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offPower", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:OOPower:OFFPower \n
		Snippet: value: str = driver.applications.k14Xnr5G.calculate.limit.ooPower.offPower.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the results of the limit check in the 'Off' periods of On/Off Power measurements. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: results: Returns one value for every 'Off' period. PASSED Limit check has passed. FAILED Limit check has failed."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:OOPower:OFFPower?')
		return trim_str_response(response)
