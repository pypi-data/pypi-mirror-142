from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tolerance:
	"""Tolerance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tolerance", core, parent)

	def set(self, limit: str, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:TOLerance \n
		Snippet: driver.applications.k91Wlan.calculate.limit.tolerance.set(limit = '1', window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines or queries the tolerance limit to be used for the measurement. The required tolerance limit depends
		on the used standard. \n
			:param limit: 'Prior802_11_2012' Tolerance limits are based on the IEEE 802.11 specification prior to 2012. Default for OFDM standards (except 802.11ac) . 'Std802_11_2012' Tolerance limits are based on the IEEE 802.11 specification from 2012. Required for DSSS standards. Also possible for OFDM standards (except 802.11ac) . 'P802_11acD5_1' Tolerance limits are based on the IEEE 802.11ac specification. Required by IEEE 802.11ac standard. 'P802_11axD0_1' Tolerance limits are based on the IEEE 802.11ax specification. Required by IEEE 802.11ax standard. 'P802_11beD0_1' Tolerance limits are based on the IEEE 802.11be specification. Required by IEEE 802.11be standard.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.value_to_quoted_str(limit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TOLerance {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:TOLerance \n
		Snippet: value: str = driver.applications.k91Wlan.calculate.limit.tolerance.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines or queries the tolerance limit to be used for the measurement. The required tolerance limit depends
		on the used standard. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit: 'Prior802_11_2012' Tolerance limits are based on the IEEE 802.11 specification prior to 2012. Default for OFDM standards (except 802.11ac) . 'Std802_11_2012' Tolerance limits are based on the IEEE 802.11 specification from 2012. Required for DSSS standards. Also possible for OFDM standards (except 802.11ac) . 'P802_11acD5_1' Tolerance limits are based on the IEEE 802.11ac specification. Required by IEEE 802.11ac standard. 'P802_11axD0_1' Tolerance limits are based on the IEEE 802.11ax specification. Required by IEEE 802.11ax standard. 'P802_11beD0_1' Tolerance limits are based on the IEEE 802.11be specification. Required by IEEE 802.11be standard."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TOLerance?')
		return trim_str_response(response)
