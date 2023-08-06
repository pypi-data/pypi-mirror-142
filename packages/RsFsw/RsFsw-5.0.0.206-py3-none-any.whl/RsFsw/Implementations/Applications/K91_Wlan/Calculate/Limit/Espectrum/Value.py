from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, power: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:VALue \n
		Snippet: driver.applications.k91Wlan.calculate.limit.espectrum.value.set(power = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param power: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(power)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:VALue {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:VALue \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.limit.espectrum.value.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: power: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:VALue?')
		return Conversions.str_to_float(response)
