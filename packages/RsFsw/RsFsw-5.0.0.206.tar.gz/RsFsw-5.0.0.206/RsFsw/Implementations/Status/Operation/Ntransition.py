from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ntransition:
	"""Ntransition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntransition", core, parent)

	def set(self, summary_bit: int) -> None:
		"""SCPI: STATus:OPERation:NTRansition \n
		Snippet: driver.status.operation.ntransition.set(summary_bit = 1) \n
		These commands control the Negative TRansition part of a register. Setting a bit causes a 1 to 0 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:param summary_bit: No help available
		"""
		param = Conversions.decimal_value_to_str(summary_bit)
		self._core.io.write(f'STATus:OPERation:NTRansition {param}')

	def get(self) -> int:
		"""SCPI: STATus:OPERation:NTRansition \n
		Snippet: value: int = driver.status.operation.ntransition.get() \n
		These commands control the Negative TRansition part of a register. Setting a bit causes a 1 to 0 transition in the
		corresponding bit of the associated register. The transition also writes a 1 into the associated bit of the corresponding
		EVENt register. \n
			:return: summary_bit: No help available"""
		response = self._core.io.query_str(f'STATus:OPERation:NTRansition?')
		return Conversions.str_to_int(response)
