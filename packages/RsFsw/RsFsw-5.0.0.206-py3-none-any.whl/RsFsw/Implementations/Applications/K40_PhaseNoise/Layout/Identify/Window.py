from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def get(self, window_name: str) -> int:
		"""SCPI: LAYout:IDENtify[:WINDow] \n
		Snippet: value: int = driver.applications.k40PhaseNoise.layout.identify.window.get(window_name = '1') \n
		This command queries the index of a particular display window in the active channel. Note: to query the name of a
		particular window, use the LAYout:WINDow<n>:IDENtify? query. \n
			:param window_name: String containing the name of a window.
			:return: window_index: Index number of the window."""
		param = Conversions.value_to_quoted_str(window_name)
		response = self._core.io.query_str_with_opc(f'LAYout:IDENtify:WINDow? {param}')
		return Conversions.str_to_int(response)
