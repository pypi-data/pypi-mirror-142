from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Link:
	"""Link commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("link", core, parent)

	def set(self, links: str, window=repcap.Window.Default) -> None:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig:LINK \n
		Snippet: driver.applications.k149Uwb.sense.window.display.rwConfig.link.set(links = '1', window = repcap.Window.Default) \n
		Links a list of windows to this window. If a window exists in another set of linked windows, they are removed from that
		set. \n
			:param links: 1..n Window
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.value_to_quoted_str(links)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig:LINK {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig:LINK \n
		Snippet: value: str = driver.applications.k149Uwb.sense.window.display.rwConfig.link.get(window = repcap.Window.Default) \n
		Links a list of windows to this window. If a window exists in another set of linked windows, they are removed from that
		set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: links: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig:LINK?')
		return trim_str_response(response)
