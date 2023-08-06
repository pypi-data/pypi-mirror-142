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
		Snippet: value: int = driver.applications.k60Transient.display.wselect.get() \n
		No command help available \n
			:return: active_window: No help available"""
		response = self._core.io.query_str(f'DISPlay:WSELect?')
		return Conversions.str_to_int(response)
