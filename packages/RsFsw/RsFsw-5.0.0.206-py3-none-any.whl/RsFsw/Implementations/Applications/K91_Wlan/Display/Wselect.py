from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wselect:
	"""Wselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wselect", core, parent)

	def get(self) -> int:
		"""SCPI: DISPlay:WSELect \n
		Snippet: value: int = driver.applications.k91Wlan.display.wselect.get() \n
		This command queries the currently active window (the one that is focused) in the currently selected measurement channel. \n
			:return: selected_window: Index number of the currently active window. Range: 1 to 16"""
		response = self._core.io.query_str(f'DISPlay:WSELect?')
		return Conversions.str_to_int(response)
