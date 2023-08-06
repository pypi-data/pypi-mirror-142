from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Domain:
	"""Domain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("domain", core, parent)

	def set(self, span_setting: enums.SpanSetting, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol:DOMain \n
		Snippet: driver.calculate.limit.control.domain.set(span_setting = enums.SpanSetting.FREQuency, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command selects the domain of the limit line. \n
			:param span_setting: FREQuency | TIME FREQuency For limit lines that apply to a range of frequencies. TIME For limit lines that apply to a period of time.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(span_setting, enums.SpanSetting)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:DOMain {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.SpanSetting:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol:DOMain \n
		Snippet: value: enums.SpanSetting = driver.calculate.limit.control.domain.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command selects the domain of the limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: span_setting: FREQuency | TIME FREQuency For limit lines that apply to a range of frequencies. TIME For limit lines that apply to a period of time."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:DOMain?')
		return Conversions.str_to_scalar_enum(response, enums.SpanSetting)
