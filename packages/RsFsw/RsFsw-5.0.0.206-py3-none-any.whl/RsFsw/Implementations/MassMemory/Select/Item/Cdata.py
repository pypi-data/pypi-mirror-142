from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdata:
	"""Cdata commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdata", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:CDATa \n
		Snippet: driver.massMemory.select.item.cdata.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:ITEM:CDATa {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:SELect[:ITEM]:CDATa \n
		Snippet: value: bool = driver.massMemory.select.item.cdata.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'MMEMory:SELect:ITEM:CDATa?')
		return Conversions.str_to_bool(response)
