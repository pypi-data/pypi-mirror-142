from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Final:
	"""Final commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("final", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:FINal \n
		Snippet: driver.massMemory.select.item.final.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:ITEM:FINal {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:SELect[:ITEM]:FINal \n
		Snippet: value: bool = driver.massMemory.select.item.final.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'MMEMory:SELect:ITEM:FINal?')
		return Conversions.str_to_bool(response)
