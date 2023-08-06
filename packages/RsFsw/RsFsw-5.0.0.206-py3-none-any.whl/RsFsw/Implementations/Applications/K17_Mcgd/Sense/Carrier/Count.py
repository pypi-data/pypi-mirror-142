from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:CARRier:COUNt \n
		Snippet: driver.applications.k17Mcgd.sense.carrier.count.set(count = 1.0) \n
		Sets/queries the number of carriers. \n
			:param count: integer
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:CARRier:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CARRier:COUNt \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.carrier.count.get() \n
		Sets/queries the number of carriers. \n
			:return: count: integer"""
		response = self._core.io.query_str(f'SENSe:CARRier:COUNt?')
		return Conversions.str_to_float(response)
