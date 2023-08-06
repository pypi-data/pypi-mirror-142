from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, average_count: float) -> None:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: driver.applications.k10Xlte.sense.average.count.set(average_count = 1.0) \n
		No command help available \n
			:param average_count: No help available
		"""
		param = Conversions.decimal_value_to_str(average_count)
		self._core.io.write(f'SENSe:AVERage:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: value: float = driver.applications.k10Xlte.sense.average.count.get() \n
		No command help available \n
			:return: average_count: No help available"""
		response = self._core.io.query_str(f'SENSe:AVERage:COUNt?')
		return Conversions.str_to_float(response)
