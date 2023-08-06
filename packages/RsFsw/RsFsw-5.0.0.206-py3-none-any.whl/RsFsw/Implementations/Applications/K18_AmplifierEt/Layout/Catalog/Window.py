from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def get(self) -> List[str]:
		"""SCPI: LAYout:CATalog[:WINDow] \n
		Snippet: value: List[str] = driver.applications.k18AmplifierEt.layout.catalog.window.get() \n
		This command queries the name and index of all active windows in the active channel from top left to bottom right.
		The result is a comma-separated list of values for each window, with the syntax: <WindowName_1>,<WindowIndex_1>..
		<WindowName_n>,<WindowIndex_n> \n
			:return: result: No help available"""
		response = self._core.io.query_str_with_opc(f'LAYout:CATalog:WINDow?')
		return Conversions.str_to_str_list(response)
