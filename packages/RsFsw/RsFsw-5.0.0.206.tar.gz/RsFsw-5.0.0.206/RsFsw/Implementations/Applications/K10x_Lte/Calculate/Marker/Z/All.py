from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:Z:ALL \n
		Snippet: value: float = driver.applications.k10Xlte.calculate.marker.z.all.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the marker position on the z-axis of three-dimensional result displays. Instead of returning a
		certain type of value (EVM, Power or Allocation ID) , which is possible with method RsFsw.Applications.K10x_Lte.Calculate.
		Marker.Z.get_, this command returns all types of values (EVM, Power and Allocation ID) , regardless of the result display
		type. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: position: numeric value EVM EVM at the marker position. Power Power at the marker position. Allocation ID Allocation ID at the marker position. Modulation Modulation type at the marker position."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:Z:ALL?')
		return Conversions.str_to_float(response)
