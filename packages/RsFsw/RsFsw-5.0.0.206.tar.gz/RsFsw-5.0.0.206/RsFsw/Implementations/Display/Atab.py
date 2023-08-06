from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atab:
	"""Atab commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atab", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: DISPlay:ATAB \n
		Snippet: driver.display.atab.set(state = False) \n
		This command switches between the MultiView tab and the most recently displayed channel. If only one channel is active,
		this command has no effect. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:ATAB {param}')

	def get(self) -> bool:
		"""SCPI: DISPlay:ATAB \n
		Snippet: value: bool = driver.display.atab.get() \n
		This command switches between the MultiView tab and the most recently displayed channel. If only one channel is active,
		this command has no effect. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'DISPlay:ATAB?')
		return Conversions.str_to_bool(response)
