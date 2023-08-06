from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: FETCh:PTABle:ACP:ACHannel<ch>:BALanced:MAXimum:Y[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.ptable.acp.achannel.balanced.maximum.y.result.get(window = repcap.Window.Default) \n
		These commands query the result values for the ACP Balanced result as shown in the Parameter Sweep Table. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: results: numeric value • For ...[:RESult]: Minimum or maximum result that has been measured. • For ...:X[:RESult]: Location on the x-axis where the minimum or maximum result has been measured. The type of value depends on the parameter you have selected for the x-axis (method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.X.Setting.set) . • For ...:Y[:RESult]: Location on the y-axis where the minimum or maximum result has been measured. The type of value depends on the parameter you have selected for the y-axis (method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Y.Setting.set) ."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh:PTABle:ACP:ACHannel{window_cmd_val}:BALanced:MAXimum:Y:RESult?')
		return Conversions.str_to_float(response)
