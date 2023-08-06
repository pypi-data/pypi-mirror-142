from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: FETCh<n>:SUMMary:XCORr:MLOBe:WIDTh:MINimum \n
		Snippet: value: float = driver.applications.k149Uwb.fetch.summary.xcorr.mlobe.width.minimum.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: result: numeric value"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh{window_cmd_val}:SUMMary:XCORr:MLOBe:WIDTh:MINimum?')
		return Conversions.str_to_float(response)
