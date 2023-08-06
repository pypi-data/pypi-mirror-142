from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbol:
	"""Symbol commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbol", core, parent)

	def set(self, symbol: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:SYMBol \n
		Snippet: driver.applications.k91Wlan.calculate.marker.symbol.set(symbol = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command positions the selected marker to the indicated symbol. This command is query only for the following result
		displays:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Constellation vs Symbol
			- Constellation vs Carrier \n
			:param symbol: integer
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(symbol)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SYMBol {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:SYMBol \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.marker.symbol.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command positions the selected marker to the indicated symbol. This command is query only for the following result
		displays:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Constellation vs Symbol
			- Constellation vs Carrier \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: symbol: integer"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SYMBol?')
		return Conversions.str_to_float(response)
