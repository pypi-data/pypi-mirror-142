from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit:MACCuracy:RHO:MEAN[:RESult] \n
		Snippet: value: str = driver.applications.k70Vsa.calculate.limit.maccuracy.rho.mean.result.get(window = repcap.Window.Default) \n
		This command queries whether the limit for the specified result type and limit type was violated. For details on result
		types and limit types see 'Result summary'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: result: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit:MACCuracy:RHO:MEAN:RESult?')
		return trim_str_response(response)
