from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, result: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:Y \n
		Snippet: driver.applications.k10Xlte.calculate.marker.y.set(result = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the position of a marker on the y-axis. In result displays with a third aspect (for example 'EVM vs
		Symbol x Carrier') , you can also use the command to define the position of the marker on the y-axis. If necessary, the
		command activates the marker first. To get a valid result, you have to perform a complete measurement with
		synchronization to the end of the measurement before reading out the result. This is only possible for single measurement
		mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param result: numeric value Result at the marker position. The type of value and its unit depend on the selected result display.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(result)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:Y \n
		Snippet: value: float = driver.applications.k10Xlte.calculate.marker.y.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the position of a marker on the y-axis. In result displays with a third aspect (for example 'EVM vs
		Symbol x Carrier') , you can also use the command to define the position of the marker on the y-axis. If necessary, the
		command activates the marker first. To get a valid result, you have to perform a complete measurement with
		synchronization to the end of the measurement before reading out the result. This is only possible for single measurement
		mode. See also method RsFsw.Applications.K10x_Lte.Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: result: numeric value Result at the marker position. The type of value and its unit depend on the selected result display."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Y?')
		return Conversions.str_to_float(response)
