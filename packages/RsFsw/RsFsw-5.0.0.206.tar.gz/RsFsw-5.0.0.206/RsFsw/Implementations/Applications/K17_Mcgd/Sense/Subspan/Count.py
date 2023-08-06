from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, subspan_count: float) -> None:
		"""SCPI: [SENSe]:SUBSpan:COUNt \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.count.set(subspan_count = 1.0) \n
		Defines the number of subspans for active frequency subspan measurements. \n
			:param subspan_count: numeric value
		"""
		param = Conversions.decimal_value_to_str(subspan_count)
		self._core.io.write(f'SENSe:SUBSpan:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SUBSpan:COUNt \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.subspan.count.get() \n
		Defines the number of subspans for active frequency subspan measurements. \n
			:return: subspan_count: numeric value"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:COUNt?')
		return Conversions.str_to_float(response)
