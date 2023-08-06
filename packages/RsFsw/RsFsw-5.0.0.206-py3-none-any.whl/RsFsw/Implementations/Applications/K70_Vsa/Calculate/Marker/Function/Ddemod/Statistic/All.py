from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> str:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:DDEMod:STATistic:ALL \n
		Snippet: value: str = driver.applications.k70Vsa.calculate.marker.function.ddemod.statistic.all.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		The command queries all results of the result summary. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: results: Comma-separated list of result values in the order described below. Note the last rows differ from the Result Summary display."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:DDEMod:STATistic:ALL?')
		return trim_str_response(response)
