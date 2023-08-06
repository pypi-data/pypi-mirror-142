from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, arg_0: str) -> None:
		"""SCPI: LAYout:REMove[:WINDow] \n
		Snippet: driver.applications.k14Xnr5G.layout.remove.window.set(arg_0 = '1') \n
		This command removes a window from the display in the active channel. \n
			:param arg_0: String containing the name of the window. In the default state, the name of the window is its index.
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write_with_opc(f'LAYout:REMove:WINDow {param}')

	def get(self) -> str:
		"""SCPI: LAYout:REMove[:WINDow] \n
		Snippet: value: str = driver.applications.k14Xnr5G.layout.remove.window.get() \n
		This command removes a window from the display in the active channel. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str_with_opc(f'LAYout:REMove:WINDow?')
		return trim_str_response(response)
