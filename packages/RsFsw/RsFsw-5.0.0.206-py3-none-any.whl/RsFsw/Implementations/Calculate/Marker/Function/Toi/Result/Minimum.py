from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:TOI:RESult:MINimum \n
		Snippet: value: float = driver.calculate.marker.function.toi.result.minimum.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command queries the results for the minimum third order intercept point measurement (see 'TOI results') . To get a
		valid result, you have to perform a complete measurement with synchronization to the end of the measurement before
		reading out the result. This is only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.
		Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: toi: Minimum third order intercept point."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:TOI:RESult:MINimum?')
		return Conversions.str_to_float(response)
