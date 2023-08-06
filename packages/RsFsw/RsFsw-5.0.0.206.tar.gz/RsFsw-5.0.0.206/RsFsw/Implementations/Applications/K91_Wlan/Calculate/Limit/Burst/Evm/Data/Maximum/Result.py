from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.LimitCheck:
		"""SCPI: CALCulate<n>:LIMit<li>:BURSt:EVM:DATA:MAXimum:RESult \n
		Snippet: value: enums.LimitCheck = driver.applications.k91Wlan.calculate.limit.burst.evm.data.maximum.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command returns the result of the average or maximum EVM limit check for data carriers. The limit value is defined
		by the standard or the user (see method RsFsw.Applications.K91_Wlan.Calculate.Limit.Burst.Evm.Data.Maximum.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit_check: PASS | FAILed PASS The defined limit for the parameter was not exceeded. FAILED The defined limit for the parameter was exceeded."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:BURSt:EVM:DATA:MAXimum:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.LimitCheck)
