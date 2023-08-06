from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfrequency:
	"""Cfrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfrequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:EMI:CFRequency \n
		Snippet: driver.diagnostic.service.inputPy.emi.cfrequency.set(frequency = 1.0) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:EMI:CFRequency {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SERVice:INPut:EMI:CFRequency \n
		Snippet: value: float = driver.diagnostic.service.inputPy.emi.cfrequency.get() \n
		No command help available \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:EMI:CFRequency?')
		return Conversions.str_to_float(response)
