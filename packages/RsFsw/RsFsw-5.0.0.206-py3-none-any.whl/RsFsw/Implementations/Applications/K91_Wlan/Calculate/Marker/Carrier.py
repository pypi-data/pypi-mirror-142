from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	def set(self, carrier_no: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:CARRier \n
		Snippet: driver.applications.k91Wlan.calculate.marker.carrier.set(carrier_no = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command positions the selected marker to the indicated carrier. This command is query only for the following result
		displays:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Constellation vs Symbol
			- Constellation vs Carrier \n
			:param carrier_no: integer
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(carrier_no)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:CARRier {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:CARRier \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.marker.carrier.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command positions the selected marker to the indicated carrier. This command is query only for the following result
		displays:
			INTRO_CMD_HELP: The .csv file has the following structure: \n
			- Constellation vs Symbol
			- Constellation vs Carrier \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: carrier_no: integer"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:CARRier?')
		return Conversions.str_to_float(response)
