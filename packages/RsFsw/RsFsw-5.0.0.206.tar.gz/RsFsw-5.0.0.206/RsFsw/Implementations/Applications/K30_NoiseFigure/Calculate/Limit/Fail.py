from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fail:
	"""Fail commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fail", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:FAIL \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.calculate.limit.fail.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the result of a limit check in the specified window. To get a valid result, you have to perform a
		complete measurement with synchronization to the end of the measurement before reading out the result. This is only
		possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: result: 0 PASS 1 FAIL"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:FAIL?')
		return Conversions.str_to_bool(response)
