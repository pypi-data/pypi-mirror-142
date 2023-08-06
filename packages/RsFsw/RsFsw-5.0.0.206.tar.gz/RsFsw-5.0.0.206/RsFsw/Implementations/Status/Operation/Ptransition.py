from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptransition:
	"""Ptransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptransition", core, parent)

	def set(self, summary_bit: int) -> None:
		"""SCPI: STATus:OPERation:PTRansition \n
		Snippet: driver.status.operation.ptransition.set(summary_bit = 1) \n
		These commands control the Positive TRansition part of a register. Setting a bit causes a 0 to 1 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:param summary_bit: No help available
		"""
		param = Conversions.decimal_value_to_str(summary_bit)
		self._core.io.write(f'STATus:OPERation:PTRansition {param}')

	def get(self) -> int:
		"""SCPI: STATus:OPERation:PTRansition \n
		Snippet: value: int = driver.status.operation.ptransition.get() \n
		These commands control the Positive TRansition part of a register. Setting a bit causes a 0 to 1 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:return: summary_bit: No help available"""
		response = self._core.io.query_str(f'STATus:OPERation:PTRansition?')
		return Conversions.str_to_int(response)
