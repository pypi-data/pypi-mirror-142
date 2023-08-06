from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, carr_count: float) -> None:
		"""SCPI: [SENSe]:SUBSpan:CARRier:COUNt \n
		Snippet: driver.applications.k17Mcgd.sense.subspan.carrier.count.set(carr_count = 1.0) \n
		Defines the bandwidth of the subspans in number of carriers for active frequency subspan measurements. \n
			:param carr_count: numeric value
		"""
		param = Conversions.decimal_value_to_str(carr_count)
		self._core.io.write(f'SENSe:SUBSpan:CARRier:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SUBSpan:CARRier:COUNt \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.subspan.carrier.count.get() \n
		Defines the bandwidth of the subspans in number of carriers for active frequency subspan measurements. \n
			:return: carr_count: numeric value"""
		response = self._core.io.query_str(f'SENSe:SUBSpan:CARRier:COUNt?')
		return Conversions.str_to_float(response)
