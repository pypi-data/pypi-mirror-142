from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Weighting:
	"""Weighting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("weighting", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect:CHANnel[:ITEM]:WEIGhting \n
		Snippet: driver.massMemory.select.channel.item.weighting.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:CHANnel:ITEM:WEIGhting {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:SELect:CHANnel[:ITEM]:WEIGhting \n
		Snippet: value: bool = driver.massMemory.select.channel.item.weighting.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'MMEMory:SELect:CHANnel:ITEM:WEIGhting?')
		return Conversions.str_to_bool(response)
