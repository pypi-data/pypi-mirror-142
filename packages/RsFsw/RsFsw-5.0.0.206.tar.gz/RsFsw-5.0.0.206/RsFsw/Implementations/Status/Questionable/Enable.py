from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, summary_bit: int) -> None:
		"""SCPI: STATus:QUEStionable:ENABle \n
		Snippet: driver.status.questionable.enable.set(summary_bit = 1) \n
		These commands control the ENABle part of a register. The ENABle part allows true conditions in the EVENt part of the
		status register to bereported in the summary bit. If a bit is 1 in the enable register and its associated event bit
		transitions to true, a positive transition will occur in the summary bit reported to the next higher level. \n
			:param summary_bit: No help available
		"""
		param = Conversions.decimal_value_to_str(summary_bit)
		self._core.io.write(f'STATus:QUEStionable:ENABle {param}')

	def get(self) -> int:
		"""SCPI: STATus:QUEStionable:ENABle \n
		Snippet: value: int = driver.status.questionable.enable.get() \n
		These commands control the ENABle part of a register. The ENABle part allows true conditions in the EVENt part of the
		status register to bereported in the summary bit. If a bit is 1 in the enable register and its associated event bit
		transitions to true, a positive transition will occur in the summary bit reported to the next higher level. \n
			:return: summary_bit: No help available"""
		response = self._core.io.query_str(f'STATus:QUEStionable:ENABle?')
		return Conversions.str_to_int(response)
