from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default) -> List[float]:
		"""SCPI: CALCulate<n>:MARKer:FUNCtion:POWer:RESult \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.calculate.marker.function.power.result.get(window = repcap.Window.Default) \n
		This command queries the (numerical) results of the ACLR measurement. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: powers: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:MARKer:FUNCtion:POWer:RESult?')
		return response
