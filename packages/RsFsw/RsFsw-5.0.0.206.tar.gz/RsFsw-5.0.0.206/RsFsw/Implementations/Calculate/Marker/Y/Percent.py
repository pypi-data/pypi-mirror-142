from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Percent:
	"""Percent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("percent", core, parent)

	def set(self, probability: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:Y:PERCent \n
		Snippet: driver.calculate.marker.y.percent.set(probability = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command sets a marker to a particular probability value. You can query the corresponding level with method RsFsw.
		Applications.K10x_Lte.Calculate.Marker.X.set. Using the command turns delta markers into normal markers. This command is
		available for CCDF measurements. \n
			:param probability: Range: 0 % to 100 %, Unit: %
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(probability)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y:PERCent {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:Y:PERCent \n
		Snippet: value: float = driver.calculate.marker.y.percent.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command sets a marker to a particular probability value. You can query the corresponding level with method RsFsw.
		Applications.K10x_Lte.Calculate.Marker.X.set. Using the command turns delta markers into normal markers. This command is
		available for CCDF measurements. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: probability: Range: 0 % to 100 %, Unit: %"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y:PERCent?')
		return Conversions.str_to_float(response)
