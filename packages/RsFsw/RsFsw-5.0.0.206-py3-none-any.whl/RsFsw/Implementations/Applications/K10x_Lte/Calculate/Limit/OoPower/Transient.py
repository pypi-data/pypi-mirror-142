from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transient:
	"""Transient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transient", core, parent)

	def get(self, result: enums.ResultTypeE, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:OOPower:TRANsient \n
		Snippet: value: str = driver.applications.k10Xlte.calculate.limit.ooPower.transient.get(result = enums.ResultTypeE.ALL, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the results of the limit check during the transient periods of the On/Off power measurement. \n
			:param result: ALL Queries the overall limit check results. FALLing Queries the limit check results of falling transients. RISing Queries the limit check results of rising transients.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit_check: Returns one value for every 'Off' period. PASSED Limit check has passed. FAILED Limit check has failed."""
		param = Conversions.enum_scalar_to_str(result, enums.ResultTypeE)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:OOPower:TRANsient? {param}')
		return trim_str_response(response)
