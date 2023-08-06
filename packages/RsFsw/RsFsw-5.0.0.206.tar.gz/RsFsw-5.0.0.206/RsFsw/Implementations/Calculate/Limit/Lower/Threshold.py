from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, threshold: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:LOWer:THReshold \n
		Snippet: driver.calculate.limit.lower.threshold.set(threshold = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines a threshold for relative limit lines. The R&S FSW uses the threshold for the limit check, if the
		limit line violates the threshold. \n
			:param threshold: Numeric value. The unit depends on method RsFsw.Calculate.Limit.Unit.set. Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(threshold)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:LOWer:THReshold {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:LOWer:THReshold \n
		Snippet: value: float = driver.calculate.limit.lower.threshold.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines a threshold for relative limit lines. The R&S FSW uses the threshold for the limit check, if the
		limit line violates the threshold. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: threshold: Numeric value. The unit depends on method RsFsw.Calculate.Limit.Unit.set. Unit: DBM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:LOWer:THReshold?')
		return Conversions.str_to_float(response)
