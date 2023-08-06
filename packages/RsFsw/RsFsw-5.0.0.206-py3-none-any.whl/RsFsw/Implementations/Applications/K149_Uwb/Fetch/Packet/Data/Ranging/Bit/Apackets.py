from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apackets:
	"""Apackets commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apackets", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: FETCh<n>:PACKet:DATA:RANGing:BIT:APACkets \n
		Snippet: value: str = driver.applications.k149Uwb.fetch.packet.data.ranging.bit.apackets.get(window = repcap.Window.Default) \n
		Returns whether the value of SFD is the same (IDEN) or not (MIX) for all packets. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: Window"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:PACKet:DATA:RANGing:BIT:APACkets?')
		return trim_str_response(response)
