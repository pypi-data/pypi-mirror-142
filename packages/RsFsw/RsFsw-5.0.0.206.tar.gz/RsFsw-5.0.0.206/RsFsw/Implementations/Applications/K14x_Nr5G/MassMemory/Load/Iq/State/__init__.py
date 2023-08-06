from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def set(self, state: List[int]) -> None:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: driver.applications.k14Xnr5G.massMemory.load.iq.state.set(state = [1, 2, 3]) \n
		This command restores I/Q data from a file. \n
			:param state: String containing the path and name of the source file.
		"""
		param = Conversions.list_to_csv_str(state)
		self._core.io.write(f'MMEMory:LOAD:IQ:STATe {param}')

	def get(self) -> List[int]:
		"""SCPI: MMEMory:LOAD:IQ:STATe \n
		Snippet: value: List[int] = driver.applications.k14Xnr5G.massMemory.load.iq.state.get() \n
		This command restores I/Q data from a file. \n
			:return: state: No help available"""
		response = self._core.io.query_bin_or_ascii_int_list(f'MMEMory:LOAD:IQ:STATe?')
		return response

	def clone(self) -> 'State':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = State(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
