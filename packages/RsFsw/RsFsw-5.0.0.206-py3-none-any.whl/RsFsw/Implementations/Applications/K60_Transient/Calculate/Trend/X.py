from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:TRENd:X \n
		Snippet: value: str = driver.applications.k60Transient.calculate.trend.x.get(window = repcap.Window.Default) \n
		Queries the x-axis parameter used for the specified Parameter Trend result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: xaxis: Name of the parameter displayed on the x-axis of the trend display. For a description of the parameters see 'Chirp parameter trends' and 'Hop parameter trends'."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRENd:X?')
		return trim_str_response(response)
