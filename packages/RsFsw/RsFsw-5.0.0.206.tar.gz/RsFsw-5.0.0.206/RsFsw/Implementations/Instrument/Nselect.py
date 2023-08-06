from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nselect:
	"""Nselect commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nselect", core, parent)

	def set(self, option_number: int) -> None:
		"""SCPI: INSTrument:NSELect \n
		Snippet: driver.instrument.nselect.set(option_number = 1) \n
		No command help available \n
			:param option_number: No help available
		"""
		param = Conversions.decimal_value_to_str(option_number)
		self._core.io.write_with_opc(f'INSTrument:NSELect {param}')

	def get(self) -> int:
		"""SCPI: INSTrument:NSELect \n
		Snippet: value: int = driver.instrument.nselect.get() \n
		No command help available \n
			:return: option_number: No help available"""
		response = self._core.io.query_str_with_opc(f'INSTrument:NSELect?')
		return Conversions.str_to_int(response)
