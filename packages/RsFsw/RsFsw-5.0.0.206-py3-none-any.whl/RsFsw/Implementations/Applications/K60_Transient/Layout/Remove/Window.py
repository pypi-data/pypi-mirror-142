from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, window_name: str) -> None:
		"""SCPI: LAYout:REMove[:WINDow] \n
		Snippet: driver.applications.k60Transient.layout.remove.window.set(window_name = '1') \n
		This command removes a window from the display in the active channel. \n
			:param window_name: String containing the name of the window. In the default state, the name of the window is its index.
		"""
		param = Conversions.value_to_quoted_str(window_name)
		self._core.io.write_with_opc(f'LAYout:REMove:WINDow {param}')
