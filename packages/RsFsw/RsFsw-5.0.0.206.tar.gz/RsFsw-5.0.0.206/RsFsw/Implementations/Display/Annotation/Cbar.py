from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbar:
	"""Cbar commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbar", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: DISPlay:ANNotation:CBAR \n
		Snippet: driver.display.annotation.cbar.set(state = False) \n
		This command hides or displays the channel bar information. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:ANNotation:CBAR {param}')

	def get(self) -> bool:
		"""SCPI: DISPlay:ANNotation:CBAR \n
		Snippet: value: bool = driver.display.annotation.cbar.get() \n
		This command hides or displays the channel bar information. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'DISPlay:ANNotation:CBAR?')
		return Conversions.str_to_bool(response)
