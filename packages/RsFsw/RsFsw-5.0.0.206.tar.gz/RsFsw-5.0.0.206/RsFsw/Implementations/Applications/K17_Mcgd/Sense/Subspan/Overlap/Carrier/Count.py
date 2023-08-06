from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, overlap_count: float) -> None:
		"""SCPI: [SENSe]:SUBSpan:OVERlap:CARRier:COUNt \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.overlap.carrier.count.set(overlap_count = 1.0) \n
		Defines the overlap of subspans in carriers for active frequency subspan measurements. \n
			:param overlap_count: numeric value
		"""
		param = Conversions.decimal_value_to_str(overlap_count)
		self._core.io.write(f'SENSe:SUBSpan:OVERlap:CARRier:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SUBSpan:OVERlap:CARRier:COUNt \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.subspan.overlap.carrier.count.get() \n
		Defines the overlap of subspans in carriers for active frequency subspan measurements. \n
			:return: overlap_count: No help available"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:OVERlap:CARRier:COUNt?')
		return Conversions.str_to_float(response)
